# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from fang.items import NewHouseItem,OldHouseItem

class CrwalFangtianxiaSpider(CrawlSpider):
    name = 'crwal_fangtianxia'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']
    #
    rules = (
        Rule(LinkExtractor(allow=r'https://www.fang.com/SoufunFamily.htm'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        trs = response.xpath('//div[@id="c02"]//tr')
        #遇到有空格的判断 或者下面那部分都属于它 那么首先建一个局部变量 =None
        province = None
        for tr in trs:
            #xpath中表示标签没有属性的语法：not(@class)来区分同样的标签
            province_text = tr.xpath('./td[not(@class)]//text()').get()
            province_text = re.sub('[\s]','',province_text)
            # 这里表示 如果有内容 那么None等于之前的省份内容
            if province_text:
                province = province_text

            if province == ('其它'):
                #continue表示不再爬下去 停止
                continue

            city_data = tr.xpath('./td/a')
            for i in city_data:
                city = i.xpath('./text()').get()
                if city == '昌吉':
                    continue

                city_url = i.xpath('./@href').get()
                url_split = city_url.split('.')
                url_header = url_split[0]
                #如果bj在里面
                if 'bj' in url_header:
                    newhouse_url = 'https://newhouse.fang.com/house/s/'
                    oldhouse_url = 'https://esf.fang.com/house/i31/'
                    # newcity_url = url_header + '.newhouse' + '.' + url_split[1] + '.' + url_split[2] + 'house/s/ '
                else:
                    newhouse_url = url_header + '.newhouse.fang.com/house/s/'
                    oldhouse_url = url_header + '.esf.fang.com/house/i31/'


                    #传参用的方法是meta={'info':(,)} 两个数据的时候就用元组传出去
                    yield scrapy.Request(url=newhouse_url,callback=self.parse_newhouse,meta={'info':(province,city)})
                    #可以传多次yield  callback=self.parse_oldhouse#这个注意
                    yield scrapy.Request(url=oldhouse_url,callback=self.parse_oldhouse,meta={'info':(province,city)})
                    # break
            # break

    def parse_newhouse(self,response):
        # 进行接参数的命令  元组的接收方法 直接写在一起 用逗号分开 后面需要从meta里面去参数 那么使用response.meta.get('info')
        province, city = response.meta.get('info')
        #首先为了使数据紧凑 使用遍历最好
        nl_cons = response.xpath('//div[contains(@class,"nl_con ")]/ul/li')
        for nl_con in nl_cons:
            name = nl_con.xpath('.//div[@class="nlcd_name"]/a/text()').get()
            if name == None:
                continue
            name = re.sub('\s','',name)
            rooms = "".join(nl_con.xpath('.//div[contains(@class,"house_type")]/a/text()').getall())
            area = "".join(nl_con.xpath('.//div[contains(@class,"house_type")]/text()').getall())
            area = re.sub('[\s/－]','',area)
            district = "".join(nl_con.xpath('.//div[@class="address"]//text()').getall())
            # if district == None:
            #     continue
            #正则取[]中间的值
            district = re.search('.*\[(.+)\].*',district).group(1)

            address = nl_con.xpath('.//div[@class="address"]/a/@title').get()
            sale = nl_con.xpath('.//div[contains(@class,"fangyuan")]/span/text()').get()
            house = ",".join(nl_con.xpath('.//div[contains(@class,"fangyuan")]/a/text()').getall())
            house = re.sub('[\s]','',house)
            price = "".join(nl_con.xpath('.//div[@class="nhouse_price"]//text()').getall())
            price = re.sub('[\s]','',price)
            phone = "".join(nl_con.xpath('.//div[@class="tel"]//text()').getall())
            phone = re.sub('[\s]','',phone)
            origin_url = nl_con.xpath('.//div[@class="nlcd_name"]/a/@href').get()
            # print(response.urljoin(origin_url))
            item = NewHouseItem(province=province,city=city,name=name,rooms=rooms,area=area,district=district,address=address,sale=sale,
                                house=house,price=price,phone=phone,origin_url=response.urljoin(origin_url))
            yield item

        next_url_data = response.xpath('//div[@class="page"]')
        if '上一页' in next_url_data.xpath('.//a[@class="next"]/text()').get():
            next_url = next_url_data.xpath('.//a[14][@class="next"]/@href').get()
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_newhouse, dont_filter=True,
                                 meta={'info': (province, city)})

        elif '下一页' in next_url_data.xpath('.//a[@class="next"]/text()').get():
            next_url = next_url_data.xpath('.//a[@class="next"]/@href').get()
            print(response.urljoin(next_url))
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_newhouse, dont_filter=True,
                                 meta={'info': (province, city)})

        else:
            return
        # if 'house/s/b91/' in base_url:
        #     next_url = re.sub('b91', 'b92', base_url)
        #     yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_newhouse, dont_filter=True,
        #                          meta={'info': (province, city)})
        #
        # else:
        #     next_url = response.xpath('//div[@id="list_D10_15"]/p[3]/a/@href').get()
        #     print(next_url)
        #     yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_newhouse, dont_filter=True,
        #                          meta={'info': (province, city)})



    def parse_oldhouse(self,response):

        #进行接参数的命令  元组的接收方法 直接写在一起 用逗号分开 后面需要从meta里面去参数 那么使用response.meta.get('info')
        province,city = response.meta.get('info')
        #这是开始 需要进行遍历数据 同步的将各种信息搭配
        #其中因为shop_list为共存的class属性名 所以需要使用('//div[contains(@class,"shop_list")]/dl')
        shop_lists  = response.xpath('//div[contains(@class,"shop_list")]/dl')
        #遍历
        for shop_list in shop_lists:

            name = shop_list.xpath('.//p[@class="add_shop"]/a/@title').get()
            if name == None:
                continue
            # rooms_data = "".join(shop_list.xpath('.//p[@class="tel_shop"]/text()').getall())
            # rooms_data = re.sub('[\s]','',rooms_data)

            rooms_data = shop_list.xpath('.//p[@class="tel_shop"]/text()').getall()
            #这里使用map方法 因为后面的filter的使用需要一个列表 然后使用lambda函数来遍历 再用正则表达式来去除空格
            rooms_data = list(map(lambda x:re.sub('[\s]','',x),rooms_data))
            #filter中的endswith方法
            rooms = list(filter(lambda i:i.endswith('厅'),rooms_data))
            area = list(filter(lambda i:i.endswith('㎡'),rooms_data))
            floors = list(filter(lambda i:i.endswith('）'),rooms_data))
            direction = list(filter(lambda i:i.endswith('向'),rooms_data))
            year = list(filter(lambda i:i.endswith('建'),rooms_data))
            address = shop_list.xpath('.//p[@class="add_shop"]/span/text()').get()
            fang_msg = ",".join(shop_list.xpath('.//p[contains(@class,"clearfix")]//text()').getall())
            fang_msg = re.sub('[\s]','',fang_msg)
            price_data = "".join(shop_list.xpath('.//dd[@class="price_right"]//text()').getall())
            price_data = re.sub('[\s]', '', price_data).split('万')
            price = price_data[0] + '万,' +price_data[1]
            people = shop_list.xpath('.//span[@class="people_name"]/a/text()').get()
            item = OldHouseItem(province=province,city=city,rooms=rooms,area=area,floors=floors,direction=direction,year=year,address=address,
                                fang_msg=fang_msg,price=price,people=people)
            yield item

        base_url = response.url
        # for i in range(1,100):
        #     next_url = base_url%i

        if 'house/i31/' in base_url :
            next_url = re.sub('i31','i32',base_url)
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_oldhouse, dont_filter=True,
                                 meta={'info': (province, city)})

        else:
            next_url = response.xpath('//div[@id="list_D10_15"]/p[3]/a/@href').get()
            print(next_url)
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_oldhouse, dont_filter=True,
                                 meta={'info': (province, city)})

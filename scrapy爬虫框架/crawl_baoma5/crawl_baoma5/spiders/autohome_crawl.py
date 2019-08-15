# -*- coding: utf-8 -*-
import scrapy
# 导入CrawlSpider类
from scrapy.spiders import CrawlSpider,Rule
#还需要导入link
from scrapy.linkextractors import LinkExtractor
# 导入item类
from crawl_baoma5.items import  CrawlBaoma5Item



# 旧的
# class AutohomeCrawlSpider(scrapy.Spider):
#新的继承CrawlSpider类
class AutohomeCrawlSpider(CrawlSpider):
    name = 'autohome_crawl'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    # CrawlSpider的写法
    #首先定义一个rules规则  rules=()
    rules = (
        #允许的域名  .代表后面添加的数据  +代表一个数据以上
        Rule(LinkExtractor(allow='https://car.autohome.com.cn/pic/series/65\-.+'), follow=True,callback='parse_url'),

        # Rule(LinkExtractor(allow='https://car.autohome.com.cn/photo/series.+\.html'),follow=True,callback='parse_url'),

        # Rule(LinkExtractor(allow='.+/photo/series.+\.html'), follow=True,callback='parse_url'),

    )
#失败的操作
    # def parse_url(self, response):
        # if response.url == 'https://car.autohome.com.cn/pic/series/65.+':
        # car_data_title = response.xpath("//div[@class='uibox']/div/text()").get()
        # if car_data_title == None:
        #     return
        # print("="*40)
        # print(car_data_title)
        # print("=" * 40)
        # #还没取geturl
        # # print(response.url)
        # if response.url == '.+/photo/series.+\.html':
        #     car_img_urls = response.xpath('//img[@id="img"]/@src').getall()
        #     car_img_url = list(map(lambda url:response.urljoin(url),car_img_urls))
        #     return car_img_url
        # print(car_img_url)
        # yield CrawlBaoma5Item(car_data_title=car_data_title,car_img_url=car_img_url)
        # car_img_urls = response.xpath('//img[@id="img"]/@src').getall()
#         # car_img_url = list(map(lambda url: response.urljoin(url), car_img_urls))
#         # print("=" * 40)
#         # print(car_img_url)
#         # print("=" * 40)
#         # car_data_title = response.xpath("//div[@class='uibox']/div/text()").get()
#         # if car_data_title == None:
#         #     return
#         # print("="*40)
#         # print(car_data_title)
#         # print("=" * 40)
#         # yield CrawlBaoma5Item(car_data_title=car_data_title,car_img_url=car_img_url)


    # def parse_pkg(self, responses):
    #
    #     car_data_title = responses.xpath("//div[@class='uibox']/div/text()").get()
    #     # print(car_data_title)
    #     yield CrawlBaoma5Item(car_data_title=car_data_title)


#成功爬取
    def parse_url(self, response):
        car_data_title = response.xpath("//div[@class='uibox']/div/text()").get().strip()
        print('=' * 30)
        print(car_data_title)
        print('=' * 30)
        car_img_urls = response.xpath('//ul/li/a/img/@src').getall()
        car_img_url = list(map(lambda url:response.urljoin(url.replace('t_','')),car_img_urls))
        # print('='*30)
        # print(car_img_url)
        # print('=' * 30)
        yield CrawlBaoma5Item(car_data_title=car_data_title,car_img_url=car_img_url)













    # 在crawlspide的底层中 本来就已经定义好parse了 所以这里不能出现def parse()

    # def parse(self, response):
    #     #解析数据  一般可以选择用一个整体url 然后遍历取数据
    #     xpath_data = response.xpath('//div[@class="uibox"]')[1:]
    #     for data in xpath_data:
    #         car_data_title = data.xpath('.//div[@class="uibox-title"]/a/text()').get()
    #         # print(car_data_title)
    #         car_img_urls = xpath_data.xpath('.//ul/li/a/img/@src').getall()
    #         # print(car_img_url)
    #         #第一种方法  不太好用
    #         # for i in car_img_urls:
    #         #         car_img_url = "https:" + i
    #         #         print(car_img_url)
    #
    #
    #         #第二种方法 补全img_url 使用response.urljoin()  好用  返回的是str类型
    #         # for i in car_img_urls:
    #         #     car_img_url = response.urljoin(i)
    #         #     print(type(car_img_url))
    #
    #         #第三种方法获取  利用lambda匿名函数处理  意思为后面的car_img_urls在lambda函数中url进行遍历，然后再response.urljoin(url)补全url信息
    #         # 用其中map为一个对象 所以要转list类型
    #         car_img_url = list(map(lambda url:response.urljoin(url),car_img_urls))
    #         # print(type(car_img_url))
    #
    #         #然后进行保存 这里需要用到item 和pipline
    #         #这里的car_img_url 格式问题注意返回最好是一个列表
    #         item =  CrawlBaoma5Item(car_data_title=car_data_title,car_img_url=car_img_url)
    #         yield item






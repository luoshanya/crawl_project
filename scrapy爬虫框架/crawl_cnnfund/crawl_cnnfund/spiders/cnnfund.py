# -*- coding: utf-8 -*-
import scrapy
import re
from crawl_cnnfund.items import CrawlCnnfundItem
from multiprocessing import Pool
from threading import Thread
import threading

class CnnfundSpider(scrapy.Spider,threading.Thread):
    name = 'cnnfund'
    allowed_domains = ['cnnfund.com']
    start_urls = ['http://www.cnnfund.com/login.aspx?action=login&from=']


    def start_requests(self):

        # 写入登录信息
        #底层有cookies值 编写好密码 fromrequest()里面的url是start_urls
        data = {
            'username': 'zhukelin',
            'password': '10130503',
        }
        # 发送post请求   5
        request = scrapy.FormRequest(self.start_urls[0], formdata=data, callback=self.parse)
        # 返回数据

        yield request

    def parse(self, response):
        xpath_data01 = response.xpath('//div[contains(@class,"Proclamation_main")]')

        for i in xpath_data01:
            url_data = i.xpath('.//div[contains(@class,"Proclamation_title")]/a/@href').getall()
            for i in url_data:
                url_data01 = "http://www.cnnfund.com/" + i
                request = scrapy.Request(url=url_data01,dont_filter=True,callback=self.parse_url)
                yield request

        for i in range(1,30):
            url = response.url + '?page=%s'%str(i)
            yield scrapy.Request(url,dont_filter=True,callback=self.parse)

    def parse_url(self,response):
        xpath_data02 = response.xpath('//div[contains(@class,"newdtl_title")]/text()').get()
        title = re.sub('[\s]', '', xpath_data02)
        data = "".join(response.xpath('//div[@class="newdtl_tx"]/text()').get())
        data = re.sub('[\s]', '', data).split('l')
        time_data = data[0]
        lilan_data = data[1]
        origin_data = data[2]
        # print(time_data)
        content = "".join(response.xpath('//div[@class="newdtl_content"]//text()').getall())
        content = re.sub('[\s]', '', content)
        item = CrawlCnnfundItem(title=title,time_data=time_data,lilan_data=lilan_data,origin_data=origin_data,content=content)
        yield item

if __name__ == '__main__':
    p = Pool(5)
    t = CnnfundSpider()
    for item in p.map(t.parse_url,t.parse):
        print(item)

    # for i in range(5):
    #     t = Thread(target=t.parse)
    #     t.start()
    #     t2 = Thread(target=t.parse_url)
    #     t2.start()

        # print(title)



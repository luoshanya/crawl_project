# -*- coding: utf-8 -*-
import scrapy
import os

class XinlangNewsSpider(scrapy.Spider):
    name = 'xinlang_news'
    allowed_domains = ['www.sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        datas = response.xpath('//div[@class="article"]')

        for data in datas:
            #大标题
            news_file = data.xpath('.//h3[@class="tit02"]/a/text()').getall()

            news_son_file = data.xpath('.//ul/li/a/text()').getall()
            news_url = data.xpath('.//ul/li/a/@href').getall()
            # print(news_url)

            for item in news_file:
                #遇到逐级文件夹的时候 创建一个新的目录 然后进行path路径拼接
                item_file = r'./data/' + item
                if not os.path.exists(item_file):
                    os.makedirs(item_file)
                # 小标题文件夹
                for item01 in news_son_file:
                    item01_flie = item_file + '/' + item01
                    if not os.path.exists(item01_flie):
                        os.makedirs(item01_flie)

            for url in news_url:
                # print(url)
                yield scrapy.Request(url,callback=self.parse_url,dont_filter=True)



    def parse_url(self,response):
        urls_data = response.xpath('//a/@href').getall()
        for url in urls_data:
            response_url = response.urljoin(url)
            # print(response_url)
            if_url = response_url.endswith('.html') and response_url.startswith('http://news')
            if if_url:
                print(url)
                yield scrapy.Request(response.urljoin(url),callback=self.parse_request,dont_filter=True)
    # #
    # #
    def parse_request(self,response):
        pass
        # title = response.xpath('//h1[@class="main-title"]/text()').get()
        # print(title)




# -*- coding: utf-8 -*-
import scrapy


class YaozhiSpider(scrapy.Spider):
    name = 'yaozhi'
    allowed_domains = ['yaozh.com']
    start_urls = ['https://www.yaozh.com/login/']



    def start_requests(self):
        #相当于start_url
        # url = 'https://www.yaozh.com/login/'
        #写入登录信息
        data = {
            "username": "zhukelin",
            "pwd": "as751286012",
            'formhash': '586FAADA00',
            'backurl': '%2F%2Fwww.yaozh.com%2F'


        }
        #发送post请求   5
        request = scrapy.FormRequest(self.start_urls[0],formdata=data,callback=self.parse)
        #返回数据
        yield request
    def parse(self, response):
        # print(response.text)
        #只是账号没被激活 就是这样发送post请求的
        with open('yaozhiwang1.html','w',encoding='utf-8') as f:
            f.write(response.text)
        url = 'https://www.yaozh.com/member/'
        data = scrapy.Request(url,callback=self.parse_url)
        yield data

    def parse_url(self,response):
        print(response.text)
        with open('yaozhiwang.html','wb',encoding='utf-8') as f:
            f.write(response.text)
            pass
# -*- coding: utf-8 -*-
import scrapy
import json

class UseragentSpider(scrapy.Spider):
    name = 'useragent'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/user-agent']

    # 随机请求头
    def parse(self, response):
        user_agent = json.loads(response.text)['user-agent']
        print(user_agent)
        #dont_filter=True 属于去重 就是说url重复的话就不会去请求 所以需要就设置True
        yield scrapy.Request(self.start_urls[0],dont_filter=True)



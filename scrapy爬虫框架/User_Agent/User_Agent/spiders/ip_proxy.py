# -*- coding: utf-8 -*-
import scrapy
import json

class IpProxySpider(scrapy.Spider):
    name = 'ip_proxy'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        IP_proxy = json.loads(response.text)['origin']
        print(IP_proxy)
        yield scrapy.Request(self.start_urls[0],dont_filter=True)

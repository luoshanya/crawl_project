# -*- coding: utf-8 -*-
import scrapy
import json

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=d9caec966e7792e27cd857b5a11cd675&desktop=true&page_number=2']

    def parse(self, response):
        print("=" * 30)
        print(response.url)
        t = json.loads(response.text)
        print("="*30)
        print(t)


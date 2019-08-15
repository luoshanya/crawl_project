# -*- coding: utf-8 -*-
import scrapy


class CrawlmaitianSpider(scrapy.Spider):
    name = 'crawlMaitian'
    allowed_domains = ['http://bj.maitian.cn/esfall/PG1']
    start_urls = ['http://http://bj.maitian.cn/esfall/PG1']

    def parse(self, response):
        pass

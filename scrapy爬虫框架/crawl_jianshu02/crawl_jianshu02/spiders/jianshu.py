# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
import re

class JianshuSpider(CrawlSpider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    start_urls= ['https://www.jianshu.com/p/04d180d90a3f']
    # start_urls = []
    # for i in range(1):
    #     start_urls.append(start_url.format(i))

    rules = (
        Rule(LinkExtractor(allow=r'/p/.+'),callback='parse_url',follow=True),
    )



    def parse_url(self, response):
        content = "".join(response.xpath('//div[@class="show-content-free"]//text()').getall())
        content = re.sub("[]")

        # content = response.xpath('div[@class="show-content-free"]/p/text()').getall()
        print(content)

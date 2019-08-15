# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from crawl_biquge.items import CrawlBiqugeItem


class BqgDpcqSpider(CrawlSpider):
    name = 'bqg_dpcq'
    allowed_domains = ['022003.com']
    start_urls = ['http://www.022003.com/2_2447/']

    rules = (
        Rule(LinkExtractor(allow=r'/2_2447/[0-9]{6}.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath('//div[@class="bookname"]/h1/text()').get()
        content = "".join(response.xpath('//div[@id="content"]/text()').getall()).strip()
        content = re.sub('[\n\xa0\u3000]','',content).split('http')[0]
        item = CrawlBiqugeItem(title=title,content=content)
        yield item



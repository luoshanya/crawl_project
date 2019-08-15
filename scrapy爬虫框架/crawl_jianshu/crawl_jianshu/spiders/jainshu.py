# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from crawl_jianshu.items import CrawlJianshuItem
import re

class JainshuSpider(CrawlSpider):
    name = 'jainshu'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/p/979790d15dbe']

    rules = (
        #.*代表可有可无   [0-9a-z]{12}代表由0-9和a-z的数字和英语组成的12位字符串
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_url', follow=True),
    )

    def parse_url(self, response):
        title = response.xpath('//div[@class="article"]/h1/text()').get()
        author = response.xpath('//span[@class="name"]/a/text()').get()
        avatar = response.xpath('//a[@class="avatar"]/img/@src').get()
        pub_time = response.xpath('//span[@class="publish-time"]/text()').get().replace('*','')
        origin_url = response.url
        url_one = origin_url.split('?')[0]
        article_id = origin_url.split('/')[-1]
        content = "".join(response.xpath('//div[@class="show-content-free"]//text()').getall()).strip()
        content = re.sub('[\n]','',content)
        item = CrawlJianshuItem(
            title=title,
            author=author,
            avatar=avatar,
            pub_time=pub_time,
            origin_url=response.url,
            article_id=article_id,
            content=content
        )
        yield item

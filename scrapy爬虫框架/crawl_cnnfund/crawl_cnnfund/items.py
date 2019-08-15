# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlCnnfundItem(scrapy.Item):
    title = scrapy.Field()
    time_data = scrapy.Field()
    lilan_data = scrapy.Field()
    origin_data = scrapy.Field()
    content = scrapy.Field()

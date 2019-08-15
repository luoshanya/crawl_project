# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlBaoma5Item(scrapy.Item):
    car_data_title = scrapy.Field()
    car_img_url = scrapy.Field()

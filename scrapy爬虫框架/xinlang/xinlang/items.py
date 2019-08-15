# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XinlangItem(scrapy.Item):
    #第一步分类文件夹
    news_file = scrapy.Field()
    new_file_url = scrapy.Field()
    #所包含的子类名称
    news_son_file = scrapy.Field()
    #所包含的子类url入口
    news_url = scrapy.Field()
    #每个文章的url
    content_url = scrapy.Field()

    #每个文章的详情页
    title = scrapy.Field()
    content = scrapy.Field()



# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewHouseItem(scrapy.Item):
    #省份
    province = scrapy.Field()
    #城市
    city = scrapy.Field()
    #楼盘名
    name = scrapy.Field()
    #几居 这里很有可能是一个列表
    rooms = scrapy.Field()
    #面积
    area = scrapy.Field()
    #行政区
    district = scrapy.Field()
    #地址
    address = scrapy.Field()
    #待售情况
    sale = scrapy.Field()
    #什么类型的房源
    house = scrapy.Field()
    #多少钱一平方
    price = scrapy.Field()
    #电话号码
    phone = scrapy.Field()
    #新房的url
    origin_url = scrapy.Field()

#建一个存储二手房的类
class OldHouseItem(scrapy.Item):
    #省
    province = scrapy.Field()
    #城市
    city = scrapy.Field()
    #楼盘的名字
    name = scrapy.Field()
    #几房几厅
    rooms = scrapy.Field()
    #面积
    area = scrapy.Field()
    #层数
    floors = scrapy.Field()
    #坐向
    direction = scrapy.Field()
    #新建时间
    year = scrapy.Field()
    #地址
    address = scrapy.Field()
    #其他信息
    fang_msg = scrapy.Field()
    #价格
    price = scrapy.Field()
    #用户出售
    people = scrapy.Field()


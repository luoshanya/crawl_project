# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlQcwyItem(scrapy.Item):
    #工作名称
    job_name = scrapy.Field()
    #学历
    education = scrapy.Field()
    #工作详情页面url
    job_name_url = scrapy.Field()
    #详情页爬取
    #公司名字
    company = scrapy.Field()
    #地区
    city_district = scrapy.Field()
    #工作经验
    work_experience = scrapy.Field()
    #招几人
    employ_data = scrapy.Field()
    #发布时间
    introduced_time = scrapy.Field()
    #职位信息
    work_describe = scrapy.Field()
    #职位类别
    work_type = scrapy.Field()
    #公司地址
    company_address = scrapy.Field()
    #公司信息
    company_message = scrapy.Field()
    #公司福利
    company_welfare = scrapy.Field()
    #关键字
    keyword = scrapy.Field()
    #薪金
    salary = scrapy.Field()


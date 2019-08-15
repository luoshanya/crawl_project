# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlZhilianItem(scrapy.Item):
    city = scrapy.Field()
    jobName = scrapy.Field()
    eduLevel = scrapy.Field()
    updateDate = scrapy.Field()
    endDate = scrapy.Field()
    positionURL = scrapy.Field()
    welfare = scrapy.Field()
    salary = scrapy.Field()
    workingExp = scrapy.Field()
    company_size = scrapy.Field()
    company_name = scrapy.Field()
    company_type = scrapy.Field()
    jobType = scrapy.Field()
    createDate = scrapy.Field()


    emplType = scrapy.Field()
    job_people = scrapy.Field()
    job_msg = scrapy.Field()

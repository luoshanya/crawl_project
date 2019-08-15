# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from Boss.items import BossItem
class ZhipinSpider(CrawlSpider):
    name = 'zhipin'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['https://www.zhipin.com/c101280100/?query=python&page=1']

    rules = (
        #下一页的url规则
        Rule(LinkExtractor(allow=r'.+c101280100/?query=python&page=\d'), follow=True),
        #详情页url规则
        Rule(LinkExtractor(allow=r'.+job_detail/.+\.html'), follow=False,callback='parse_job'),
    )

    def parse_job(self, response):
        #以后第一步就是设置配置文件 再进行爬虫
        name = response.xpath('//div[@class="info-primary"]//h1/text()').get().strip()
        salary = response.xpath('//div[@class="info-primary"]//h1/text()').get().strip()
        jobs_data = response.xpath('//div[contains(@class,"job-primary")]/div[@class="info-primary"]/p/text()').getall()
        city = jobs_data[0]
        work_experience = jobs_data[1]
        education = jobs_data[2]
        company = response.xpath('//a[@ka="job-detail-company"]/@title').get().strip()
        desc_data = "".join(response.xpath('//div[@class="text"]/text()').getall()).strip()
        desc_data = re.sub('[\n]',"",desc_data)
        item = BossItem(name=name,salary=salary,city=city,work_experience=work_experience,education=education,company=company,desc_data=desc_data)
        yield item




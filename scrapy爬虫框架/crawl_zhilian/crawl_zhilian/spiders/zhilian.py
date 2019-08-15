# -*- coding: utf-8 -*-
import scrapy
import json
import re
import json
from crawl_zhilian.items import CrawlZhilianItem
from scrapy.shell import inspect_response

class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['sou.zhaopin.com']
    city = input('请输入你选择的城市: 广州:763 深圳:765\n')
    job = input('请输入您需要查询的职业信息:')
    education = input('请输入你的学历：-1:不限 1:其他 2:博士 3:硕士 4:本科 5:大专 6:高中/中专以下:')
    start_urls = []
    start_url = 'https://fe-api.zhaopin.com/c/i/sou?start=%s&pageSize=90&cityId={}&salary=0,0&workExperience=-1&education={}&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw={}&kt=3&=0&at=96694f2567894a85ae5b254eab349117&rt=f76a98cc0c1447179258cdd321cc3670&_v=0.67928609&userCode=1028190947&x-zp-page-request-id=5ba0cf470e4e4b9fa7ba78d6da71aa1f-1553450010792-626000'.format(education,int(city),job)
    for i in range(0,8):
        t = start_url%str(i*90)
        start_urls.append(t)

    def parse_item(self,response):

        (city,updateDate, endDate, welfare, salary, workingExp, company_size, company_name, company_type, jobType,
         createDate,jobName, eduLevel, emplType) = response.meta.get('info')
        # print(city)
        main_data = response.xpath('//div[@class="app"]')
        # print(city)
        for data in main_data:

            # dict_data['job_people'] = data.xpath('.//div[contains(@class,"info-three")]/span[4]/text()').get()
            job_people = data.xpath('.//ul[@class="summary-plane__info"]/li[4]/text()').get()
            # print(job_people)

            # job_msg= "".join(data.xpath('.//div[contains(@class,"responsibility")]//text()').getall())
            job_msg = "".join(data.xpath('.//div[@class="describtion__detail-content"]//text()').getall())

            job_msg = re.sub('[\s]','',job_msg)
            print(job_msg)
            item = CrawlZhilianItem(city=city, jobName=jobName,eduLevel=eduLevel,updateDate=updateDate,
                                    endDate=endDate, welfare=welfare,
                                    salary=salary, workingExp=workingExp,
                                    company_size=company_size, company_name=company_name,
                                    company_type=company_type,
                                    jobType=jobType, createDate=createDate,

                                    emplType=emplType,job_people=job_people,job_msg=job_msg)

            yield item


            # item = CrawlZhilianItem(job_people=job_people,job_msg=job_msg)
            # inspect_response(response,self)


    def parse(self, response):
        data = json.loads(response.text)['data']['results']
        for i in data:
            city = i['city']['display']

            updateDate = i['updateDate']
            endDate = i['endDate']
            positionURL = i['positionURL']
            welfare = i['welfare']
            salary = i['salary']
            workingExp = i['workingExp']['name']

            company_size = i['company']['size']['name']
            company_name = i['company']['name']
            company_type = i['company']['type']['name']
            jobType = i['jobType']['display']
            createDate = i['createDate']
            jobName = i['jobName']
            eduLevel = i['eduLevel']['name']
            emplType = i['emplType']

            # print(city)
            yield scrapy.Request(positionURL,dont_filter=True,callback=self.parse_item,meta={'info':(city,
            updateDate,endDate,welfare,salary,workingExp,company_size,company_name,company_type,jobType,createDate,
            jobName,eduLevel,emplType)})






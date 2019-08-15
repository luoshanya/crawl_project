# -*- coding: utf-8 -*-
import scrapy
import re
from crawl_qcwy.items import CrawlQcwyItem



class QcwyJobSpider(scrapy.Spider):
    name = 'qcwy_job'
    allowed_domains = ['search.51job.com']
    try:
        city_input = input('请输入你需要查询的城市: 广州-030200 深圳-040000\n')
        base_url_data = input('请输入你需要查询的职业:\n')
        # base_url = 'https://search.51job.com/list/030000,000000,0000,00,9,99,%s,2,{}.html'%base_url_data
        start_urls = ['https://search.51job.com/list/%s,000000,0000,00,9,99,%s,2,1.html'%(city_input,base_url_data)]
        # for i in range(1,2):
        #     url = base_url.format(i)
        #     start_urls.append(url)
    except:
        print('输入信息错误,请检查！')

    def parse(self, response):
        datas = response.xpath('//div[@class="dw_table"]')
        for data in datas:
            # job_name = data.xpath('.//span/a/@title').getall()
            job_name_url = data.xpath('.//p/span/a/@href').getall()
            # print(job_name_url)

            for url in job_name_url:
                yield scrapy.Request(url,dont_filter=True,callback=self.parse_url,meta={'info':(url)})

        urls = response.xpath('//div[@class="p_in"]')
        for i in urls:
            text = i.xpath('.//li[last()]/a/text()').get()
            # print(text)
            try:
                if '下一页' == text:
                    next_url = i.xpath('.//li[last()]/a/@href').get()
                    # print(next_url)
                    yield scrapy.Request(next_url,callback=self.parse,dont_filter=True)
            except:
                print('爬取完毕!')

    def parse_url(self,response):
        job_name_url = response.meta.get('info')
        datas = response.xpath('//div[contains(@class,"tCompany_center")]')
        for data in datas:

            job_name = data.xpath('.//div[@class="cn"]/h1/@title').get()
            # print(job_name)
            salary = data.xpath('.//div[@class="cn"]/strong/text()').get()
            company = data.xpath('.//p[@class="cname"]/a/text()').get().strip()
            msg_data = data.xpath('.//p[contains(@class,"msg")]/text()').getall()
            city_district = msg_data[0].strip()
            work_experience = msg_data[1].strip()
            education = msg_data[2].strip()
            if '人' in education:
                education = '学历不限'
                employ_data = msg_data[2].strip()
                introduced_time = msg_data[3].strip()
            else:
                employ_data = msg_data[3].strip()
                introduced_time = msg_data[4].strip()
            # print(work_experience,education,employ_data,introduced_time)
            company_welfare = ",".join(data.xpath('.//div[@class="t1"]/span/text()').getall())
            if company_welfare == '':
                company_welfare = '请在职位描述查看福利信息'
            work_type = "".join(data.xpath('.//div[@class="mt10"]/p[1]/a/text()').getall()).strip()
            work_type = re.sub('[\n\s]','',work_type)
            company_address = "".join(data.xpath('.//div[@class="tCompany_main"]/div[2]//p/text()').getall())
            company_address = re.sub('[\n\s]', '', company_address)
            company_message = "".join(data.xpath('.//div[contains(@class,"tmsg")]/text()').getall())
            company_message = re.sub('[\n\s]', '', company_message)
            keyword = ",".join(data.xpath('.//div[@class="mt10"]/p[2]/a/text()').getall())
            if keyword == '':
                keyword = '没有关键字'
            work_describe = "".join(data.xpath('.//div[contains(@class,"job_msg")]/p/text()').getall())

            item = CrawlQcwyItem(job_name=job_name,salary=salary,education=education,keyword=keyword,work_experience=work_experience,job_name_url=job_name_url,company=company,city_district=city_district,
                                 employ_data=employ_data,introduced_time=introduced_time,
                                 work_describe=work_describe,work_type=work_type,company_address=company_address,
                                 company_message=company_message,company_welfare=company_welfare)
            yield item




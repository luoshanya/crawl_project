# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter,CsvItemExporter

class CrawlQcwyPipeline_json(object):
    def __init__(self):
        self.json_file = open('软件测试_job.json','wb')
        self.exporter = JsonLinesItemExporter(self.json_file,ensure_ascii=False)

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def crawl_close(self):
        self.json_file.close()

class CrawlQcwyPipeline_csv(object):
    def __init__(self):
        self.csv_file = open('软件测试_job.csv','wb')
        self.exporter = CsvItemExporter(self.csv_file,fields_to_export=['job_name','salary','education','work_experience','keyword'
                                    ,'job_name_url','company','city_district',
                                 'employ_data','introduced_time',
                                 'work_describe','work_type','company_address',
                                 'company_message','company_welfare'])

    def process_item(self,item,spider):
        self.exporter.export_item(item)
        return item

    def crawl_close(self):
        self.exporter.finish_exporting()
        self.csv_file.close()

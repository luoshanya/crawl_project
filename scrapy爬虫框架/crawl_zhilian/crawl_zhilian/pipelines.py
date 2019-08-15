# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter,CsvItemExporter

class CrawlZhilianPipeline(object):
    def __init__(self):
        self.json_file = open('深圳python.json','wb')
        self.exporter = JsonLinesItemExporter(self.json_file,ensure_ascii=False)
    def process_item(self, item, spider):
        try:
            print(item)
            self.exporter.export_item(item)
            return item
        except:
            print('=============')

    def close_crawl(self):
        self.json_file.close()

class CrawlZhilianPipeline_csv(object):
    def __init__(self):
        self.csv_file = open('深圳python.csv','wb')
        self.exporter = CsvItemExporter(self.csv_file,fields_to_export=['city', 'jobName','eduLevel','updateDate',
                                    'endDate', 'welfare',
                                    'salary', 'workingExp',
                                    'company_size', 'company_name',
                                    'company_type',
                                    'jobType', 'createDat',
                                    'emplType','ob_people','job_msg'])
    def process_item(self, item, spider):
        # print(item)
        self.exporter.export_item(item)
        return item

    def close_crawl(self):
        #注意csv格式必须要写finish_exporting()
        self.exporter.finish_exporting()
        self.csv_file.close()


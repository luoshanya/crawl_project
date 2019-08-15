# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
class BossPipeline(object):
    def __init__(self):
        self.json_file = open('jobs.json','wb')
        self.export = JsonLinesItemExporter(self.json_file,ensure_ascii=False)
    def process_item(self, item, spider):
        self.export.export_item(item)

    def request_close(self):
        self.json_file.close()


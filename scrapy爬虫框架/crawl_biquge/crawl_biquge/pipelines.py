# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import threading
from scrapy.exporters import JsonLinesItemExporter
class CrawlBiqugePipeline(object):

    def __init__(self):
        self.json = open('doupocangqiong.json','wb')
        self.exporter = JsonLinesItemExporter(self.json,ensure_ascii=False)
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def process_threading(self):
        t1 = threading.Thread()
    def process_close(self):
        self.json.close()





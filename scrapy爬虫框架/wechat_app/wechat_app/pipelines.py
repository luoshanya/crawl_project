# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exporters import JsonLinesItemExporter
class WechatAppPipeline(object):
    def __init__(self):
        self.json = open('wechat.json','wb')
        #Json写入器
        self.json_export = JsonLinesItemExporter(self.json,ensure_ascii=False,encoding='utf-8')
    def run(self):
        print("爬虫开始")
    def process_item(self, item, spider):
        self.json_export.export_item(item)
        return item
    def close_spider(self):
        self.json.close()
        print("爬虫结束")

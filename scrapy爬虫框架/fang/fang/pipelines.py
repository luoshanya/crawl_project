# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from fang.items import NewHouseItem,OldHouseItem
from scrapy.exporters import JsonLinesItemExporter
class FangPipeline(object):
    def __init__(self):
        self.new_json = open('new_house.json','wb')
        self.old_json = open('old_house.json','wb')
        self.exporter = JsonLinesItemExporter(self.new_json,ensure_ascii=False)
        self.exporters = JsonLinesItemExporter(self.old_json, ensure_ascii=False)
    def process_item(self, item, spider):
        #如果要进行两个item插入 需要使用isinstance来判断存储的对应位置
        if isinstance(item,NewHouseItem):
            self.exporter.export_item(item)
        elif isinstance(item,OldHouseItem):
            self.exporters.export_item(item)
        return item

    def close_spider(self,spider):
        self.new_json.close()
        self.old_json.close()

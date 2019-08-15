# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

#第一种方法   原始方法
# class CsbkPipeline(object):
#     def __init__(self):
#         self.json = open('csbk.json','w',encoding='utf-8')
#     def open_spider(self,spider):
#         print('爬虫开始')
#
#
#     #传过来的数据给item
#     def process_item(self, item, spider):
#         #需要保存字典类型dict()
#         json_data = json.dumps(dict(item),ensure_ascii=False)
#         self.json.write(json_data+'\n')
#
#     def close_spider(self,spider):
#         #结束爬虫
#         self.json.close()
#         print('爬虫结束')





# from scrapy.exporters import JsonItemExporter
#第二种方法  建议数据量小的时候用  返回列表[{},{}]这种类型
# class CsbkPipeline(object):
#     def __init__(self):
#         #这里创建的写入方法要写'wb'不然报错   TypeError: write() argument must be str, not bytes 还有后面不需要再编码
#         self.json = open('csbk.json','wb')
#         #JSON的导入器
#         self.export = JsonItemExporter(self.json,ensure_ascii=False,encoding='utf-8')
#         #开始导入数据
#         self.export.start_exporting()
#     def open_spider(self,spider):
#         print('爬虫开始')
#
#
#     #传过来的数据给item
#     def process_item(self, item, spider):
#         #导入export_item数据
#         self.export.export_item(item)
#
#     def close_spider(self,spider):
#         #完成导入数据
#         self.export.finish_exporting()
#         # 结束爬虫
#         self.json.close()
#         print('爬虫结束')









#第三种方法  建议数据量比较大的时候用  返回字典类型{},{}

from scrapy.exporters import JsonLinesItemExporter

class CsbkPipeline(object):
    def __init__(self):
        #这里创建的写入方法要写'wb'不然报错   TypeError: write() argument must be str, not bytes 还有后面不需要再编码
        self.json = open('csbk.json','wb')
        #JSON的导入器
        self.export = JsonLinesItemExporter(self.json,ensure_ascii=False,encoding='utf-8')
        #开始导入数据  不需要开始这个步骤
        # self.export.start_exporting()
    def open_spider(self,spider):
        print('爬虫开始')


    #传过来的数据给item
    def process_item(self, item, spider):
        #导入export_item数据  这步依然要
        self.export.export_item(item)
        return item
    def close_spider(self,spider):
        #完成导入数据   这个方法不需要完成导入命令
        # self.export.finish_exporting()
        # 结束爬虫
        self.json.close()
        print('爬虫结束')
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
class CrawlBaoma5Pipeline(object):
    def __init__(self):
        #文件目录
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'imgs')

        #判断是否存在目录
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def process_item(self, item, spider):
       try: # 然后进行遍历 url 和 title
            title = item['car_data_title']
            # title = item
            print('=' * 40)
            print(title)
            print('=' * 40)

            urls = item['car_img_url']
            print(urls)
            path_data = os.path.join(self.path,title)
            print('=' * 50)
            print(path_data)
            print('=' * 50)
            #定义存放各种类型的车图片目录  分类
            if not os.path.exists(path_data):
                os.makedirs(path_data)
            # img_name = "".join(urls.split('__')[-1].strip())
            # print(img_name)
            for url in urls:
                # print('=' * 50)
                # print(url.split('__')[-1])
                # print('=' * 50)
                img_name = "".join(url.split('__')[-1])
                print('=' * 50)
                print(img_name)
                print('=' * 50)
                #
                request.urlretrieve(url,os.path.join(path_data,img_name))
       except Exception as e:
        print(e)



        return item

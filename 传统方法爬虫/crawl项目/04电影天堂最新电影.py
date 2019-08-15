import requests
from lxml import etree
import html5lib
import csv
import json
import pymongo
from bs4 import BeautifulSoup
class movies_heaven_crawl():
    def __init__(self):
        self.url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'
        # self.url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_3.html'
        self.headers = {
            "User-Agent" : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        self.list = []
    #全部的url
    def all_url(self):
        list_data = []
        for i in range(1,10):

            url = self.url.format(i)
            # print(url)
            list_data.append(url)

        #需要返回数据，不然后面不传不了数据
        return list_data
    #还需要导进一个url才行，因为需要一个个网址的来爬取
    def crawl_request_data(self,url):
        data = requests.get(url,headers=self.headers,verify=False).content
        return data
    #数据解析
    def xpath_data(self,data):
        # soup = BeautifulSoup(data,'html5lib')
        # bs4_data = soup.select('.co_content8 ul')
        # # print(bs4_data)
        #
        # for i in bs4_data:
        #
        #     print(i.td.string)
        lxml_data = etree.HTML(data)
        xpath_data = lxml_data.xpath('//div[@class="co_content8"]/ul')
        # print(xpath_data)

        for i in xpath_data:
            dict_data = {}
            dict_data['最新影片'] = i.xpath('.//b/a/text()')[0]
            dict_data['最新时间'] = i.xpath('.//font//text()')[0]
            dict_data['下载链接'] = i.xpath('.//b/a/@href')[0]
            self.list.append(dict_data)
        print(self.list)



    def save_json(self):
        json_data = json.dump(self.list,open('04电影天堂最新电影.json','w',encoding='utf-8'))


    def save_csv(self):
        # #打开json文件
        # json_data = open('04电影天堂最新电影.json','r')
        # #创建新的csv文件
        # csv_file = open('04电影天堂最新电影.csv','w')
        #
        #
        # #读取json文件，并且换list类型  因为；还是文件类型所以需要用load()
        # read_json_data = json.load(json_data)
        # json_data_keys = read_json_data[0].keys()
        # list_data = []
        # #这里遍历的是数据不是表头
        # for i in read_json_data:
        #     list_data.append(i.values())
        #
        #
        # #csv写入器
        # write = csv.writer(csv_file)
        # #导入表头
        # write.writerow(json_data_keys)
        # #导入内容
        # write.writerows(list_data)
        pass




    # 存取MongoDB数据库
    def python_mongo(self,):
        try:#链接MongoDB数据库
            mongo_python = pymongo.MongoClient()

            #创建数据库
            db = mongo_python['heaven_movies']

            #创建表
            collection_db = db['news_movies']

            #插入数据
            collection_db.insert_many(self.list)
        except Exception as e:
            print(e)
        finally:
            mongo_python.close()


    def run(self):
        url_list = self.all_url()
        for i in url_list:
            print(i)
            data = self.crawl_request_data(i)

        #分析数据
            result = self.xpath_data(data)
            print(result)
        # self.python_mongo()
        self.save_json()
        self.save_csv()

movies_heaven_crawl().run()
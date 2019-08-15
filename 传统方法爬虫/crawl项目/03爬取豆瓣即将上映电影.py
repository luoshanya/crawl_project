import requests
from lxml import etree
import json
import csv
class Spider_newsMoviser():
    def __init__(self):
        self.url = 'https://movie.douban.com/cinema/later/guangdong/'
        self.headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        self.list = []
        #发送请求
    def Spider_requests(self,url):
        data = requests.get(url,headers=self.headers,verify=False).text
        return data
        #解析数据
    def xpath_data(self,data):
        #lxml解析数据
        lxml_data = etree.HTML(data)
        #选择器
        xpath_data = lxml_data.xpath('//div[@class="intro"]')
        for i in xpath_data:
            dict_data = {}
            dict_data['影名'] = i.xpath('./h3/a/text()')[0]
            dict_data['时间'] = i.xpath('./ul/li[1]/text()')[0]
            dict_data['类型'] = i.xpath('./ul/li[2]/text()')[0]
            dict_data['影片出处'] = i.xpath('./ul/li[3]/text()')[0]
            dict_data['多少人想看'] = i.xpath('./ul/li/span/text()')[0]
            self.list.append(dict_data)
        # print(self.list)

    def save_json_data(self):
        json_data = json.dump(self.list,open('豆瓣即将上映影片.json','w',encoding='utf-8'),ensure_ascii=False)


    def save_csv_data(self):
        #首先得打开json文件 才可以将json转换为csv格式
        open_json_data = open('豆瓣即将上映影片.json','r',)
        #创建csv文件,主要这里不用转utf-8格式 不然会乱码
        create_csv_data = open('豆瓣即将上映的影片.csv','w')

        #读取内容，需要将json转换为list类型
        read_json_data = json.load(open_json_data,ensure_ascii=True)

        #需要插入表头，所以得从json文件中提取出来
        json_data_keys = read_json_data[0].keys()
        # print(json_data_keys)
        list_data = []
        for i in read_json_data:
            list_data.append(i.values())
            # print(list_data)

        #创建写入器
        write = csv.writer(create_csv_data)

        #写入表头是row  写入内容是rows

        write.writerow(json_data_keys)
        write.writerows(list_data)

    def run(self):
        data = self.Spider_requests(self.url)
        self.xpath_data(data)
        self.save_json_data()
        self.save_csv_data()

Spider_newsMoviser().run()
import requests
import csv
import lxml
from lxml import etree
from bs4 import BeautifulSoup
import pymongo
#创建类
class Spider_douban():
    #1.得到url和headers
    def __init__(self):

        self.url = 'https://movie.douban.com/cinema/nowplaying/guangdong/'
        self.headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        self.list_data = []
    #2.发送请求
    def Spider_request(self,url):
        data = requests.get(url,self.headers,verify=False).content.decode('utf-8')
        return data

    #3.解析数据

    def Spider_xpath(self,data):
        lxml_data = etree.HTML(data)
        #取属性的值只需要写
        xpath_data = lxml_data.xpath('//div[@id="nowplaying"]//ul[@class="lists"]/li')

        #<li id="26213252" class="list-item" data-title="惊奇队长" data-score="7.2" data-star="35" data-release="2019"
        # data-duration="124分钟" data-region="美国" data-director="安娜·波顿 瑞安·弗雷克" data-actors="布丽·拉尔森 / 裘德·洛 / 塞缪尔·杰克逊"
        #  data-category="nowplaying" data-enough="True" data-showed="True" data-votecount="8534" data-subject="26213252">

        for i in xpath_data:
            dict_data = {}
            dict_data['名字'] = i.xpath('./@data-title')[0]
            dict_data['评分'] = i.xpath('./@data-score')[0]
            dict_data['多少个明星'] = i.xpath('./@data-star')[0]
            dict_data['年份'] = i.xpath('./@data-release')[0]
            dict_data['时长'] = i.xpath('./@data-duration')[0]
            dict_data['国家'] = i.xpath('./@data-region')[0]
            dict_data['导演'] = i.xpath('./@data-director')[0]
            dict_data['主演'] = i.xpath('./@data-actors')[0]
            self.list_data.append(dict_data)

        # print(self.list_data)
        # bs4_data = BeautifulSoup(data,'lxml')
        #
        # result = bs4_data.select('#nowplaying data-title')
        # result = bs4_data.find_all(name="data-title")
        # result = bs4_data.find(attrs={'class':'list-item'})


    def format_data(self):
        import json
        json_data = json.dump(self.list_data,open('豆瓣.json','w',encoding='utf-8'),ensure_ascii=False)

    def json_csv(self):
        import json
        # 1.打开json文件 创建一个CSV文件
        open_json_data = open('豆瓣.json', 'r')
        # 格式不对utf-8,pycharm里面可以看到内容，但是如果在Windows系统上看表格就会乱码，不写结果则反过来
        create_csv = open('豆瓣电影.csv', 'w')

        # 2.读取文件内容，将内容转换列表
        json_data = json.load(open_json_data)
        # 表头需要指定的内容，不能直接放进；列表
        json_data_keys = json_data[0].keys()
        data = []
        for i in json_data:
            # values(内容) 将i循环的数据放进data里
            data.append(i.values())

        # 3.创建CSV写入器
        write = csv.writer(create_csv)

        # 4.将内容写入csv
        # 表头是row  内容用writerows
        write.writerow(json_data_keys)

        write.writerows(data)

        # 5.关闭文件
        create_csv.close()
        open_json_data.close()


    def MongoDB_save(self):
        try:
            #链接MongoDB
            mongo_python = pymongo.MongoClient()

            # 创建数据库
            db = mongo_python['douban_movies']

            collection_movies = db['movies']

            collection_movies.insert_many(self.list_data)


        except Exception as e:
            print(e)

        finally:
            mongo_python.close()

    def run(self):

        data = self.Spider_request(self.url)

        self.Spider_xpath(data)

        self.format_data()
        # self.MongoDB_save()
        self.json_csv()




Spider_douban().run()
import requests
from lxml import etree
import json
from bs4 import BeautifulSoup

#第一步创建类，然后写url和headers
class crawl_start():
    def __init__(self):
        self.base_url = "http://www.allitebooks.com/page/{}"
        self.headers = {
            "User-agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        self.list_data = []
    #构建所有url
    def all_get_all(self):
        list = []
        for i in range(1, 20):
            url = self.base_url.format(i)

            list.append(url)

        return list
    #2.请求数据
    def request_data(self,url):
        data = requests.get(url,self.headers,verify=False).content.decode('utf-8')
        #记得返回数据
        return data

    #3.解析数据    <a href="http://www.allitebooks.com/digital-forensics-basics/" rel="bookmark">Digital Forensics Basics</a>
    # def xpath_data(self,data):
    #     book_data = etree.HTML(data)
    #     #首先查出有多少本书，后面才可以对书的数据进行查找
    #     book_data_list = book_data.xpath('.//div[@class="main-content-inner clearfix"]/article')
    #
    #     book_dict = {}
        #如果查很多的内容的话，一般选择遍历
        # for book in book_data_list:
        #     #书名    要取0开始 因为这是遍历，一本一本的查
        #
        #     book_dict['book_title'] = book.xpath('.//h2[@class="entry-title"]//a/text()')[0]
        #
        #     #作者
        #     book_dict['book_author'] = book.xpath('.//h5[@class="entry-author"]//a/text()')[0]
        #
        #     #图片
        #     book_dict['book_img'] = book.xpath('.//div[@class="entry-thumbnail hover-thumb"]/a/img/@src')[0]
        #
        #     #书的简历
        #     book_dict['book_content'] = book.xpath('.//div[@class="entry-summary"]/p/text()')[0]
        #     print(book_dict)
        #     self.xpath_list.append(book_dict)
            # print(self.xpath_list)

    #使用bs4来解析数据
    def bs4_data(self,data):
        bs4_data_book = BeautifulSoup(data,'lxml')

        book_list = bs4_data_book.select('article')
        for book in book_list:
            #有时候字典需要放进遍历里面，不然数据出错
            book_dict = {}
            #书名  .//h2[@class="entry-title"]//a/text()')
            book_dict['book_title'] = book.select_one('.entry-title a').get_text()
            # print(book_dict)
        #     #作者
            book_dict['book_author'] = book.select_one('.entry-author a').get_text()
        #     print(book_dict)
        #     #图片 get是抓取里面的属性get('tag 或属性')
            book_dict['book_img'] = book.select_one('.entry-thumbnail hover-thumb, a img').get('src')
        #     print(book_dict)
        #     #书的简历
            book_dict['book_content'] = book.select_one('.entry-summary p').get_text()
            # print(book_dict)
            self.list_data.append(book_dict)
        print(self.list_data)
       #4.保存数据
    def save_data(self):

        json.dump(self.list_data,open('04json.json','w',encoding='utf-8'))

    def run(self):
        #全部的url
        url_list = self.all_get_all()
        for i in url_list:

            data = self.request_data(i)
            # print(url_list)
            # self.xpath_data(data)
            reslut = self.bs4_data(data)


        self.save_data()
crawl_start().run()
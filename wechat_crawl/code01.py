from selenium import webdriver
import time
import re
from datetime import datetime
import json
import emoji

class Crawl_Wxb():
    def __init__(self):
        self.data_time = datetime.now().strftime(r'%Y-%m-%d-%H-%M-%S')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.driver = webdriver.Chrome(options=options)

    def login_wxb(self):
        self.driver.get("https://account.wxb.com/page/login?from=https://data.wxb.com/rank")
        tag = self.driver.find_element_by_xpath("//div[@class='login-type-toggle___2e_eO']/span[2]")
        tag.click()
        time.sleep(1)
        email = self.driver.find_element_by_xpath('//input[@id="email"]')
        email.send_keys('18802544885')
        pwd = self.driver.find_element_by_xpath('//input[@id="password"]')
        pwd.send_keys('as10130503')
        time.sleep(1)
        login = self.driver.find_element_by_xpath('//button[@type="button"]')
        login.click()

    def save_json(self):
        list_data = []
        for i in range(1, 51):
            time.sleep(1)
            url = "https://data.wxb.com/rank/article?baidu_cat=总榜&baidu_tag=&pageSize=50&page=%s&type=2&order=" % i
            self.driver.get(url)
            try:
                data = self.driver.page_source.encode('utf-8').decode("unicode_escape")
                res = re.match('^{?.*}}', data[121:])
                rp = re.sub(r'[\\]', '', res.group())
                data = rp[29:52]
                print(data)
                # print(data)
                list_data.append(data)
                with open('json_data/%s-data.json' % self.data_time, 'a', encoding='utf-8') as fp:
                    fp.write(rp)
            except Exception as e:
                    print(e)
        return list_data

    def get_data_id(self):
        data = self.save_json()
        for i in data:
            url = 'https://data.wxb.com/rank/articleDetail?id=%s' % i
            print(url)
            self.driver.get(url)
            time.sleep(1)
            try:
                data = self.driver.page_source.encode('utf-8').decode("unicode_escape")
                res = re.match('^{?.*}}', data[121:])
                rp = re.sub(r'[\\]', '', res.group())
                # print(rp)
                with open('json_data/%s-jd_data.json' % self.data_time, 'a', encoding='utf-8') as fp:
                    fp.write(rp)
            except Exception as e:
                print(e)

    def get_gzh_phb(self):
        for i in range(1,7):
            url = 'https://data.wxb.com/rank/day/2019-08-19/总榜?sort=&page=%s&page_size=50&is_new=1' % i
            time.sleep(1)
            self.driver.get(url)
            time.sleep(1)
            try:
                data = self.driver.page_source.encode('utf-8').decode("unicode_escape")
                print(data)
                res = re.match('^{?.*]}', data[121:])
                rp = re.sub(r'[\\]', '', res.group())
                # print(rp)
                with open('json_data/%s-公众号排行.json' % self.data_time, 'a', encoding='utf-8') as fp:
                    fp.write(rp)
            except Exception as e:
                print(e)

    def get_gzh_phbs(self):
        for i in range(1,11):
            url = 'https://data.wxb.com/rank/up/2019-08-19/总榜?sort=&page=%s&page_size=10&is_new=1' % i
            time.sleep(1)
            self.driver.get(url)
            time.sleep(1)
            try:
                data = self.driver.page_source.replace(u'\ud83d', '')
                # myre = re.compile(u'[\ud800-\udBFF][\udC00-\udFFF]')
                print(data)
                data_s= re.sub(u'[\ud800-\udBFF][\udC00-\udFFF]', '', data)
                print(data_s)
                res = re.match('^{?.*}', data[121:])
                rp = re.sub(r'[\\]', '', res.group())
                with open('json_data/%s-排名上升最快榜单.json' % self.data_time, 'a', encoding='utf-8') as fp:
                    fp.write(data)
            except Exception as e:
                print(e)

    def run(self):
        self.login_wxb()
        # self.get_data_id()
        # self.get_gzh_phb()
        self.get_gzh_phbs()

if __name__ == '__main__':
    crawl = Crawl_Wxb()
    crawl.run()
    # def get_data_id(self):
    #     try:
    #         file = open('data.json', 'r', encoding='utf-8')
    #         datas = json.load(fp=file)
    #         list_data = []
    #         for i in datas:
    #             data = i['data'][0]['id']
    #             list_data.append(data)
    #         file.close()
    #         return list_data
    #     except Exception as e:
    #         print(e)
    #
    # def get_url(self):


# import requests
#
# data = {
#     'captcha' : '',
#     'email': '18802544885',
#     'from':'',
#     'password': 'as10130503',
#     'remember': 'on'
# }
# header = {
#     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
# }
# session = requests.Session()
# response = session.post(url='http://account.wxb.com/index2/login', data=data, headers=header).content.decode('utf-8')
# print(response)
# time.sleep(1)
# da = session.get("https://data.wxb.com/rankArticle")
# data = session.get("https://data.wxb.com/rank/article?baidu_cat=%E6%80%BB%E6%A6%9C&baidu_tag=&pageSize=50&page=2&type=2&order=")
# print(da)
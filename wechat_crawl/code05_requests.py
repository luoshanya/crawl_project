import requests
import time
import re
import json
from datetime import datetime


class Crawl_wxb:
    def __init__(self):
        self.data_time = datetime.now().strftime(r'%Y-%m-%d-%H-%M-%S')
        self.data = {
            'captcha': '',
            'email': '18802544885',
            'from': '',
            'password': 'as10130503',
            'remember': 'on'
        }
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
        }
        self.cookies = {
            'aliyungf_tc': 'AQAAAD3bcjdKGQoAxUZ3cR1NLq/iYKLk',
            'visit-wxb-id' : '9974458f71a02d84511672e422dba20b',
            'Qs_pv_288791': '2013812326949126400%2C437635170583603800%2C144215348793526720',
            'RMT': '6c4d6afa3ec5f4797b7653047efa0d99',
            # 'Max-Age': 691200,
            'Qs_lvt_288791' : '1566200567',
            'RMC': 'deleted',
            'PHPSESSID' : 'd383693db13856323ede260ce66c6e15'
        }

    def login(self):
        session = requests.Session()
        response = session.post(url='http://account.wxb.com/index2/login', data=self.data, headers=self.header,
                                cookies=self.cookies).content.decode('utf-8')
        return session

    def get_gzh_s(self, session):
        list_data = []
        for i in range(1, 11):
            # time.sleep(1)
            url = 'https://data.wxb.com/rank/up/2019-08-19/总榜?sort=&page=%s&page_size=10&is_new=1' % str(i)
            data = session.get(url=url, headers=self.header, cookies=self.cookies).text
            json_data = json.loads(data)
            list_data.append(json_data)
        print(list_data)
        json.dump(fp=open('json_data/%s-排名上升.json' % self.data_time, 'w', encoding='utf-8'), obj=list_data,
                  ensure_ascii=False)

    def save_json(self, session):
        list_data = []
        list_datas = []
        for i in range(1, 51):
            # time.sleep(1)
            url = "https://data.wxb.com/rank/article?baidu_cat=总榜&baidu_tag=&page=%s&pageSize=50&type=2&order=" % i
            print(url)
            data = session.get(url=url, headers=self.header, cookies=self.cookies).text
            json_data = json.loads(data)
            list_datas.append(json_data)
            if json_data['data']:
                id_values = json_data['data'][0]['id']
                list_data.append(id_values)
        json.dump(fp=open('json_data/%s-热门文章.json' % self.data_time, 'w', encoding='utf-8'), obj=list_datas,
                  ensure_ascii=False)
        return list_data

    def get_data_id(self, session):
        data = self.save_json(session)
        list_data = []
        for i in data:
            # time.sleep(1)
            url = 'https://data.wxb.com/rank/articleDetail?id=%s' % i
            print(url)
            data = session.get(url=url, headers=self.header, cookies=self.cookies).text
            json_data = json.loads(data)
            list_data.append(json_data)
        json.dump(fp=open('json_data/%s-文章解读.json' % self.data_time, 'w', encoding='utf-8'), obj=list_data,
                  ensure_ascii=False)

    def get_gzh_phb(self, session):
        list_data = []
        for i in range(1, 7):
            url = 'https://data.wxb.com/rank/day/2019-08-19/总榜?sort=&page=%s&page_size=50&is_new=1' % i
            # time.sleep(1)
            data = session.get(url=url, headers=self.header, cookies=self.cookies).text
            json_data = json.loads(data)
            list_data.append(json_data)
        json.dump(fp=open('json_data/%s-公众号排名.json' % self.data_time, 'w', encoding='utf-8'), obj=list_data,
                  ensure_ascii=False)

    def run(self):
        session = self.login()
        # self.get_gzh_s(session)
        self.get_data_id(session)
        self.get_gzh_phb(session)


if __name__ == '__main__':
    crawl = Crawl_wxb()
    crawl.run()
# jsonpath_rew = parse('$..desc')
# res = jsonpath_rew.find(data)
# j_data = [match.value for match in res][0]
# for key,value in j_data.items():
#     # for key,value in i.items():
#     print(value)
#     print(key)

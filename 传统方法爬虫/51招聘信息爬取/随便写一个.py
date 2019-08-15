# -*- coding: utf-8 -*-


# base_url = 'https://search.51job.com/list/030000,000000,0000,00,9,99,{},2,%d.html'
# t2 = input('请输入你想查找的信息\n')
# url = base_url.format(t2)
# print(url)
import requests
from lxml import etree
import time
import re
import json

class Spider_qcwy(object):
    def __init__(self):
        self.t2 = input("请输入你想要查的职业名称：\n")
        self.base_url = 'https://search.51job.com/list/030000,000000,0000,00,9,99,{},2,%d.html'
        self.url = self.base_url.format(self.t2)
        self.headers = {
            'User-Agent' : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        self.cookies = requests.get(self.url,headers=self.headers).cookies
        self.list_data = []
        for x in range(1,8):
            url = self.url%x
            print(url)
            self.run(url)

    def run(self,url):
        response = requests.get(url,headers=self.headers,cookies=self.cookies).content.decode('gbk')
        etree_data = etree.HTML(response)
        xpath_url = etree_data.xpath('//div[@class="el"]//p//a/@href')
        for i in xpath_url:
            self.request_url(i)
            time.sleep(1)



    def request_url(self,url):
        response = requests.get(url, headers=self.headers, cookies=self.cookies).content.decode('gbk')
        etree_data = etree.HTML(response)
        position_data = etree_data.xpath('//div[@class="cn"]/h1/@title')[0]

        company_data = etree_data.xpath('//a[@class="catn"]/@title')[0]

        salary_data = etree_data.xpath('//div[@class="cn"]/strong/text()')[0]

        welfare_msg = "".join(etree_data.xpath('//div[@class="jtag"]//span/text()'))
        # print(welfare_msg)
        recruit_data = etree_data.xpath('//div[@class="cn"]/p/@title')[0].strip()
        recruit_data = re.sub('[\s]',"",recruit_data)

        desc_data = "".join(etree_data.xpath('//div[@class="tBorderTop_box"]//p/text()')).strip()
        desc_data = re.sub('[\s]',"",desc_data)

        position_category = "".join(etree_data.xpath('//p[@class="fp"]//a/text()')).strip()
        position_category = re.sub('[\s]',"",position_category)

        company_address = "".join(etree_data.xpath('//p[@class="fp"]/text()')).strip()
        # print(company_address)
        # company_address = etree_data.xpath('//a[@track-type="jobsButtonClick"]/@onclick')[-1]
        # company_address = re.sub('[()]','',company_address)
        # company_address = company_address.split(',')[1]
        # company_address = company_address.split(';')[0]
        # company_address = re.sub("['']",'',company_address)

        # company_msg = etree_data.xpath('//div[class="tCompany_main"]')
        # for i in company_msg:
        #      t = i.string().extract()
        #      print(t)
        # for a in company_msg:
        #     company_msg1 = a.xpath('.//br/text()')
        #     print(company_msg1)
        # company_msg = etree_data.xpath('//br/text')
        # print(company_msg)
        dict_data = {
            '职位' : position_data  ,
            '公司' : company_data ,
            '薪资' : salary_data ,
            '公司福利' : welfare_msg,
            '招聘信息' : recruit_data ,
            '职位信息' : desc_data,
            '职能类别' : position_category ,
            '公司地址' : company_address
        }
        print(dict_data)
        print('='*40)
        self.list_data.append(dict_data)

        json_file = json.dump(self.list_data,open('03传统抓取51职业信息.json','w',encoding='utf-8'))


if __name__ == '__main__':
    t1 = Spider_qcwy()

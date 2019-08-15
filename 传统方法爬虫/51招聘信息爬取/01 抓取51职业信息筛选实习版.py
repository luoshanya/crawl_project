import requests
from lxml import etree
import time
import re
import json

class Spider_qcwy(object):
    def __init__(self):
        self.url = 'https://search.51job.com/list/030000,000000,0000,00,9,99,%25E6%2596%2587%25E5%2591%2598,2,1.html?lang=c&stype=1&postchannel=0000&workyear=01&cotype=99&degreefrom=03&jobterm=03&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=22&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        self.headers = {
            'User-Agent' : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        self.cookies = requests.get(self.url,headers=self.headers).cookies
        self.list_data = []
        for x in range(1,8):
            url = self.url.format(x)
            self.run(url)


    def run(self,url):
        response = requests.get(url,headers=self.headers,cookies=self.cookies).content.decode('gbk')
        etree_data = etree.HTML(response)
        xpath_url = etree_data.xpath('//div[@class="el"]//p//a/@href')
        for i in xpath_url:
            self.request_url(i)
            # time.sleep(1)



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

        # company_msg = etree_data.xpath('//div[class="tCompany_main"]///br/text()').extract()
        # print(company_msg)
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

        json_file = json.dump(self.list_data,open('02抓取51通信职业信息实习版.json','w',encoding='utf-8'))


if __name__ == '__main__':
    t1 = Spider_qcwy()
    t1.run()
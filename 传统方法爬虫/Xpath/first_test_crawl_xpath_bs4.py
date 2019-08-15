import requests
from lxml import etree
from bs4 import BeautifulSoup
import json
def first_crawl_xpath_bs4():

    #输入需要的爬虫的url地址
    url = "https://www.csdn.net/"

    #输入请求头，养成好习惯
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

    #用requests发送get请求
    response = requests.get(url,headers=headers,verify=False)
    response_data = response.content.decode('utf-8')
    # print(response_data)


    #使用xpath解析数据
    xpath_response_data = etree.HTML(response_data)
    xpath_response_data_xpath = xpath_response_data.xpath('.//li[@class="clearfix"]//text()')
    print(xpath_response_data_xpath)

    # soup = BeautifulSoup(response_data,'lxml')

    # print(data)

    # soup_data = soup.get_text('div[class="summary oneline"]')



    # data_json = json.dumps(soup_data)
    # print(type(data_json))
    # print(soup_data)

first_crawl_xpath_bs4()
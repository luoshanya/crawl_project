import requests
from lxml import etree
import json
import time
import re

url_start = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
url_list = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Referer': "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
    'Connection': "keep-alive",
    'X-Anit-Forge-Code': "0",
    'X-Anit-Forge-Token': "None",
    'X-Requested-With': 'XMLHttpRequest'
}
# 以后请求cookies
cookie = requests.get(url_start, headers=headers).cookies
list_data = []
def request_data():
    data = {
        "first": "false",
        "pn": 1,
        "kd": "python"
    }
    for i in range(1):
        #替换字典中的键值对的数值
        data['pn'] = i



        # print(cookie)
        # 获取cookies
        # s = requests.Session()
        # s.get(url_start, headers=headers, timeout=3)  # 请求首页获取cookies
        # cookie = s.cookies  # 为此次获取的cookies
        # print(cookie)

        # response = requests.post(url,headers=headers,data=data,cookies=cookie).content.decode('utf-8')

        response = requests.post(url_list, headers=headers, data=data, cookies=cookie).json()

        result = response['content']['positionResult']['result']

        for position in result:
            positionID = position['positionId']

            url = 'https://www.lagou.com/jobs/%s.html'%positionID
            xpath_data(url)
            break

def xpath_data(url):
    response = requests.get(url,headers=headers).content.decode('utf-8')
    # print(response)
    dict_data = {}
    etree_data = etree.HTML(response)
    dict_data['职位名称'] = etree_data.xpath('//span[@class="name"]/text()')[0]
    dict_data['工资'] = etree_data.xpath('//span[@class="salary"]/text()')[0].strip()
    city_data = etree_data.xpath('//dd[@class="job_request"]//span/text()')[1].strip()
    dict_data['城市'] = re.sub('[\s/]',"",city_data)
    experience_data = etree_data.xpath('//dd[@class="job_request"]//span/text()')[2].strip()
    dict_data['经验'] = re.sub('[\s/]', "",experience_data)
    education_data = etree_data.xpath('//dd[@class="job_request"]//span/text()')[3].strip()
    dict_data['教育信息'] = re.sub('[\s/]', "", education_data)
    # print(education_data)
    #列表变字符串
    job_data = "".join(etree_data.xpath('//dd[@class="job-advantage"]//text()'))
    dict_data['职位诱惑'] = re.sub('[\s/]', "",job_data)
    #列表变字符串  "".join(列表放进来)
    work_data ="".join(etree_data.xpath('//dd[@class="job_bt"]//text()')).strip()
    dict_data['职位描述'] = re.sub('[\s/]', "",work_data)

    list_data.append(dict_data)
    
    # json_file = json.dump(list_data,open('拉勾网python职业信息.json','w',encoding='utf-8'))
    # print(dict_data)





def main():

    request_data()


if __name__ == '__main__':
    main()
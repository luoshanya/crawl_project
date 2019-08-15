import requests
from lxml import etree
import re
import os
from urllib import request



def parse_pgk(url):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    #第一种请求方法可以写content的写法
    # response = requests.get(url,headers=headers).content.decode('utf-8')
    #第二种方法
    response = requests.get(url,headers=headers).text

    #解析数据
    etree_data = etree.HTML(response)

    #去除属性条件，可以写！=
    xpath_data = etree_data.xpath('//div[@class="random_picture"]//img[@class!="gif"]')
    # print(xpath_data)
    for i in xpath_data:
        picture_url = i.get('data-original')
        # print(picture)
        #获取属性内容可以直接使用get('')
        alt = i.get('alt')
        # print(alt)
        # 正则表达式换符号
        alt = re.sub(r'[?？，。, .!！]','',alt)
        # print(alt)
        #使用os模块 分割文本 其中的文件名后缀也可以分割  ('https://ws4.sinaimg.cn/bmiddle/9150e4e5gy1g0s9yvo94gj20240273yf', '.jpg')
        picture_suffix = os.path.splitext(picture_url)[1]
        picture_name = alt + picture_suffix
        # print(picture_name)
        #其中使用urllib.request.urlretrieve(url,fiiename,文件名)   filename 需要使用r'下载文件路径'才行
        request.urlretrieve(picture_url,r'E:\crawl\imgs\fuck/'+picture_name)




def main():
    for i in range(1,100):
        #设定url
        url = 'http://www.doutula.com/photo/list/?page=%d'% i
        #调用函数
        parse_pgk(url)
        #只循环一次
        break

if __name__ == '__main__':
    main()
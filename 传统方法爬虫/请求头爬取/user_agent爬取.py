import requests
from lxml import etree
import json
# import io,sys
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
url = 'http://www.useragentstring.com/pages/useragentstring.php?typ=Browser'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

response = requests.get(url,headers=headers).text
etree_data = etree.HTML(response)
xpath_data = etree_data.xpath('//li/a/text()')
list_data = []
for i in xpath_data:
    dict_data = {}
    dict_data['User-Agent'] = i
    list_data.append(dict_data)

json.dump(list_data,open('User-Agent.json','w',encoding='utf-8'),ensure_ascii=False)

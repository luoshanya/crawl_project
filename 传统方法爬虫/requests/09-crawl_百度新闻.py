import re
import requests
import lxml

crawl_baidu_news_url = 'https://www.baidu.com'

headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
#只需这一步就行了 暂时不需要别的操作
crawl_get_data = requests.get(crawl_baidu_news_url,headers=headers).content.decode('utf-8')

#正则匹配开始
pattern = re.compile('<a href="(.*)">(.*)<a>',re.S)
result = pattern.findall(crawl_get_data)

#
# pattern_one = re.compile('[\u4e00-\u9fa5]+')
# result_one = pattern_one.findall(result)
print(result)

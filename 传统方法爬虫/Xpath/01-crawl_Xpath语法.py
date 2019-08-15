import re
# re正则
import requests
from lxml import etree
#引用额etree需要使用以下命令

crawl_baidu_news_url = 'https://news.baidu.com/'

headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
#只需这一步就行了 暂时不需要别的操作  需要用requests发送get请求或者post请求得到数据
crawl_get_data = requests.get(crawl_baidu_news_url,headers=headers).content.decode('utf-8')

#1.转解析类型
xpath_data = etree.HTML(crawl_get_data)
#<a href="http://www.xinhuanet.com/politics/2019-02/28/c_1124177061.htm" mon="ct=1&amp;a=2&amp;c=top&amp;pn=7" target="_blank">中央组织部原副部长李锐因病在京逝世 享年102岁</a>



#xpath 语法    1.节点/查找
#               2.跨节点查找 //
#               3.精确的标签： //a[@属性="属性值"]
#               4.标签包裹的属性text()
#               5.属性：@href
#               6.xpath--s数据类型--list
#2调用xpath方法
result = xpath_data.xpath('/html/head/title/text()')
print(result)
result = xpath_data.xpath('//a/text()')
result = xpath_data.xpath('//a[@mon="ct=1&a=2&c=top&pn=7"]/text()')
#转换成地址
result = xpath_data.xpath('//a[@mon="ct=1&a=2&c=top&pn=7"]/@href')

result = xpath_data.xpath('//li/a/text()')






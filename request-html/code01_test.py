__author__ = 'zhukelin'
__date__ = '2019/4/21 0021 上午 1:41'

from requests_html import HTMLSession


url = "https://www.lagou.com/jobs/list_%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95?labelWords=&fromSearch=true&suginput="
# 创建会话
session = HTMLSession()
# 发送请求
response = session.get(url)
print(response.text)
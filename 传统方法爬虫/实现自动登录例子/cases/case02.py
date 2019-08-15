# 模拟登录马蜂窝

import requests
from lxml import etree

#使用session会话来操持登录状态
session = requests.Session()
url = "https://passport.mafengwo.cn/login/"
phone_number = input('电话')
password = input('密码')
data = {'passport': phone_number, 'password': password, "code" : ""}
# data = {
#             "username": "18802544885",
#             "password": "y4w4DcapOhqrjsNj5HyfdNo4PK2YgwEZkqHc9NxWY9XwgcT3Bt27b9vH5Lc2uWCHu3cpr0Fx/9YoVqdy4g/NLmmbA0ano6I97CEN2FIYGFfS0P7mppwaicuJvk7SpzEI6UfqiPLXwhUeT+YIZF1Dyxh3209iviJhBuR0q7AhPS4=as10130503",
#             "verify": '',
#             "pwencode": "1",
#             "referer": "https://m.imooc.com"
#         }
header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
r = session.post(url, headers=header, data=data)
# print(r.status_code)
# print(r.json())
# print(r.content.decode("utf-8"))
#

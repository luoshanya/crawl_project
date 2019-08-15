import asyncio
import requests

# class Crawl_code():
#     def __init__(self,url):
#         self.header = {
#             "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
#             "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8"
#         }
#         self.url = url
#         # self.request_get_data = self.request_get_data()
#         # self.request_get_data02 = self.request_get_data02()
#
#     async def request_get_data(self):
#         request_get = requests.get(self.url,headers=self.header)
#         # requests_data = requests.get(url=self.url, headers=self.header)
#         # print(requests_data.text)
#         print(request_get.content.decode("utf-8"))
#
#     async def request_get_data02(self):
#         requests_data = requests.get(url=self.url, headers = self.header)
#         print(requests_data.content.decode("utf-8"))
#     def run(self):
#         asyncio.get_event_loop().run_until_complete(self.request_get_data())
#         asyncio.get_event_loop().run_until_complete(self.request_get_data02())
#
# if __name__ == '__main__':
#     url = "http://www.baidu.com"
#     crawl_code = Crawl_code(url)
#     # crawl_code.request_get_data()
#     # crawl_code.request_get_data02()
#     crawl_code.run()
#     # asyncio.get_event_loop().run_until_complete(crawl_code.request_get_data02())
#     # asyncio.get_event_loop().run_until_complete(crawl_code.request_get_data())


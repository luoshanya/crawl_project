import requests


class RequestSpider(object):
    def __init__(self):
        url = "http://www.baidu.com"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        self.response = requests.get(url,headers=header)

    def run(self):
        request_header = self.response.request.headers
        print(request_header)
        request_data = self.response.status_code
        print(request_data)
RequestSpider().run()
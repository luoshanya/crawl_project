import requests
from lxml import etree
import re

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


class Chaungye_data(object):
    def __init__(self):
        self.headers = headers
        self.list_data = []
        self.url = []
        self.base_url = 'http://www.cnnfund.com/Notification.aspx?page={}'
        for i in range(1,2):
            t = self.base_url.format(i)
            self.url.append(t)
            # print(self.url)

    #最简单的cookies登录post请求
    def run(self):
        session = requests.Session()
        login_url = 'http://www.cnnfund.com/login.aspx?action=login&from='
        data = {
            'username': 'zhukelin',
            'password': '10130503'
        }
        cookies = session.cookies
        response_login = session.post(login_url,headers=self.headers,cookies=cookies,data=data)
        print(cookies)
        self.more_url_data(cookies)
        self.chaungye_msg(cookies)

    def more_url_data(self,cookies):
        url = "http://www.cnnfund.com/"
        response = requests.get(url, headers=self.headers, cookies=cookies).text
        etree_data = etree.HTML(response)
        xpath_data = etree_data.xpath('//div[contains(@class,"fr")]/a/@href')
        urls = "http://www.cnnfund.com/{}"

    def chaungye_msg(self,cookies):
        urls = [url for url in self.url]

        for url in urls:
            response = requests.get(url,headers=self.headers,cookies=cookies).text
            etree_data01 = etree.HTML(response)
            xpath_data01 = etree_data01.xpath('//div[contains(@class,"Proclamation_main")]')
            for i in xpath_data01:
                url_data = i.xpath('.//div[contains(@class,"Proclamation_title")]/a/@href')
                for i in url_data:
                    urls_data = "http://www.cnnfund.com/" + i
                    get_data = requests.get(urls_data,headers=self.headers,cookies=cookies).text
                    etree_data02 = etree.HTML(get_data)
                    xpath_data02 = "".join(etree_data02.xpath('//div[contains(@class,"newdtl_title")]/text()'))
                    title = re.sub('[\s]','',xpath_data02)
                    content = etree_data02.xpath('//div[@class="newdtl_content"]/text()')
                    print(content)


if __name__ == '__main__':
    Chaungye_data().run()
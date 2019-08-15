# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

class ZhiHuDownloadMiddleware(object):
    User_Agent = [
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)",
        "Mozilla/5.0 (compatible; U; ABrowse 0.6;  Syllable) AppleWebKit/420+ (KHTML, like Gecko)",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X Mach-O; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-GB; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.8; it; rv:1.93.26.2658) Gecko/20141026 Camino/2.176.223 (MultiLang) (like Firefox/3.64.2268)0",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.8; it; rv:1.9.2.28) Gecko/20130628 Camino/3.245.226 (MultiLang) (like Firefox/3.621.218)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36"
    ]
    def process_request(self,request,spider):
        user_agent = random.choice(self.User_Agent)
        request.headers['User-Agent'] = user_agent



# class IpDownloadMiddleware(object):
#     PROXY_IP = [
#         'http://111.177.174.226:9999',
#         'http://111.177.162.95:9999',
#         '',
#         '',
#         '',
#     ]
#     def process_request(self,request,spider):
#         proxy_ip = random.choice(self.PROXY_IP)
#         request.meta['Proxy'] = proxy_ip

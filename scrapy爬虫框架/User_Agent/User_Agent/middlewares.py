# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import base64
class UserAgentSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class UserAgentDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class UserAgentDownloadMiddleware(object):
    USER_AGENTS = [
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
        user_agent= random.choice(self.USER_AGENTS)
        request.headers['User-Agent'] = user_agent

#设置开放代理ip代理池
# class IpProxyDownloadMiddleware():
#     #写ip地址
#     IP_PROXY = [
#         'ip',
#         'ip'
#     ]
#
#     #在建立函数
#     def process_request(self,request,spider):
#         ip_proxy = random.choice(self.IP_PROXY)
#         request.meta['proxy'] = ip_proxy


#独享代理 设置ip代理池

class IpProxyDownloadMiddleware():
    #在建立函数
    def process_request(self,request,spider):
        ip_proxy = 'ip:端口号'
        user_password = "账号:密码"   #账号和密码用冒号分开
        request.meta['proxy'] = ip_proxy
        #这里必须要导入base64包  数据类型为byte
        b64_user_password = base64.b64encode(user_password)
        #其中的 b64_user_password为byte类型 要与str类型拼接必须转类型 byte转str使用decode('utf-8)
        request.headers['Proxy-Authorization'] = 'Basic ' + b64_user_password.decode('utf-8')
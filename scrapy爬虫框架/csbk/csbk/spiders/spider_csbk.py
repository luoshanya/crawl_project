# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
#调用items.py  会出错
from csbk.items import CsbkItem

class SpiderCsbkSpider(scrapy.Spider):
    name = 'spider_csbk'
    #allowed_domains  意思：允许的域名
    allowed_domains = ['https://www.qiushibaike.com']
    #开始的url  是你需要爬取的url
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_url = "https://www.qiushibaike.com"

    def parse(self, response):

        #返回一个SelectorList数据类型 一个列表
        xpath_data = response.xpath('//div[@id="content-left"]/div')
        #进行遍历列表
        for i in xpath_data:
            #这里是每一个selector     get()是取第一个
            author = i.xpath('.//h2/text()').get().strip()
            #获取全部使用getall()
            text = i.xpath('.//div[@class="content"]//text()').getall()
            #将内容放进字符串 去空格
            text = "".join(text).strip()
            #旧的方法
            # duanzi = {'author':author,'content':text}

            #新的方法
            item = CsbkItem(author=author,content=text)
            #yield 代表一个生成器 然后把数据提交给引擎 引擎再分配
            yield item

        #如何利用下一页来获取url 重新yield scrapy.Request(url,callback='调用函数',dont_filter=True)数据 然后重新使用函数 一直往返 直到页数走完
        #找到下一页的url  并且会使用last()查找元素   记得使用get方法
        next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()
        print('='*30)
        print(next_url)
        print('=' * 30)
        # 这里需要学会使用判断语句来控制页数不存在了
        if not next_url:
            return
        else:
            #不然返回请求   yield   callback=self.parse 这个代表重复使用这个函数    使用迭代的时候 必须写dont_filter = True  在 Request 请求参数中，设置 dont_filter = True ,Request 中请求的 URL 将不通过 allowed_domains 过滤。
            yield scrapy.Request(self.base_url+next_url,callback=self.parse,dont_filter = True)
            # print(author)


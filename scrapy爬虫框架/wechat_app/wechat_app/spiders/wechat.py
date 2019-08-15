# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wechat_app.items import WechatAppItem

class WechatSpider(CrawlSpider):
    name = 'wechat'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=1&page=1']

    rules = (
    #     Rule(LinkExtractor(allow=r'http://www.wxapp-union.com/portal.php?mod=list&catid=1&page=%d'), callback='parse_item', follow=True),
    # )
        #或者前面的字符去掉 换.+ 代表前面可以任意字符 但是后面的必须相同 然后找到匹配的url    还有匹配数字的时候一定要用\d
        Rule(LinkExtractor(allow=r'.+mod=list&catid=1&page=\d'),
             follow=True),

        #第二个匹配详情页的url  为了使.没有意义 使用规则+\.  .+\.html  后面的点就是代表没有意义.html
        #不需要跟进了url 所以False    detail详情的意思
        Rule(LinkExtractor(allow=r'.+article-.+\.html'),callback="parse_detail",
             follow=False,
    )

             )
    def parse_detail(self, response):
        title = response.xpath('//h1[@class="ph"]/text()').get()
        authors = response.xpath('//p[@class="authors"]/a/text()').get()
        t_time = response.xpath('//p[@class="authors"]/span/text()').get()
        content = "".join(response.xpath('//td[@id="article_content"]//text()').getall()).strip()
        item = WechatAppItem(title=title,author=authors,time=t_time,content=content)
        yield item
__author__ = 'zhukelin'
__date__ = '2019/4/21 0021 上午 1:52'

from requests_html import AsyncHTMLSession

# 创建异步对象
asession = AsyncHTMLSession()
url_lagou = "https://www.lagou.com/"
url_boss = "https://www.zhipin.com/"
url_qcwy = "https://search.51job.com/list/030200,000000,0000,00,9,99,Python%2B%25E5%25BC%2580%25E5%258F%2591,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

# 异步请求
async def get_lagou():
    # await半等待状态
    response = await asession.get(url=url_lagou)
    return response

async def get_boss():
    response = await asession.get(url_boss)
    return response

async def get_qcwy():
    response = await asession.get(url_qcwy)
    return response

# 同时跑三个函数
results = asession.run(get_qcwy)
# print(results ,list(map(lambda x:x,results)))
for i in results:
    titles = i.html.xpath("/html/body/div(@class='dw_table')")
    for a in titles:
        title = i.html.xpath(".//a(@target='_blank')/@title")
        print(title)
    # 同时返回当前地址的url
    # print(i.html.url)

    # 抓取页面的所有url
    # links = i.html.links
    # print(links)

    # 填补url 有点像response.urljoin()的补全URL功能
    # absolute_links = i.html.absolute_links
    # print(absolute_links)

    # css_find = i.html.find(".e",first=True)
    # print(css_find.find('a'))

    # a = i.html.xpath('//a[@class="po_name"]/text()')
    # print(a)
    # for i in a:
    #     b = i.xpath('.//a[@class="po_name"]/text()')
    #     print(a)

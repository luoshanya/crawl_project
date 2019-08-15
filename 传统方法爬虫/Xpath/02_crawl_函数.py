import requests
from lxml import etree
import json
class Crawl_fisrt_Bitebi():
    #1.请求头User-Agent: 还有请求网址
    def __init__(self):
        self.url = "http://8btc.com/forum-61-"
        self.header = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        #这里可以设置全局的数据列表
        self.data_list = []
    #2.发送请求
    def get_response_url(self,url):
        # 这里的变量也可以不需要写self.
        response = requests.get(url,headers=self.header)
        #记得查看网页的编码格式 查找meta就可以看到编码格式 然后分为'gbk'与'utf-8'两种格式
        data = response.content.decode('gbk')
        #这里请求的数据data，需要return返回数据
        return data

    #3.解析请求数据

    def get_response_xpath(self,data):
        #使用xpath解析当前的页面 所以的 新闻的title 和url保存
        #1.转类型
        get_response_html = etree.HTML(data)
        #文章的title
        xpath_data_list = get_response_html.xpath('//a[@class="s xst"]/text()')
        print(xpath_data_list)
        #文章的链接 在后面加@href就行了
        xpath_data_url = get_response_html.xpath('//a[@class="s xst"]/@href')
        # pass

        #为了储存数据库或者保存，需要更好的将列表分类 一般使用遍历的方法
        # 首先设定两个参数，比较好记的就行，然后开始进行枚举 其中枚举已经将其中的字典分类为序号和内容了 其中enumerate中的参数为什么都行，但是一般为第一个比较好些
        for index,title in enumerate(xpath_data_url):
            # print(title)
            # print(index)

            xpath_data_dict = {}
            #这里下面的参数，谁写先谁就先
            xpath_data_dict['name'] = xpath_data_list[index]
            xpath_data_dict['url'] = title

            self.data_list.append(xpath_data_dict)
            #有了self.data_list全局后不需要返回数据了
            print(self.data_list)





    #3.保存数据
    #有了self.data_list全局后不需要data参数了
    def save_get_response_xpath(self):
        print(type(self.data_list))
        #需要将列表list转换为str  使用json模块
        #json模块用于转类型
        data_str = json.dumps(self.data_list)

        print(type(data_str))
        with open('05_crawl_data.json',"w",encoding='utf-8') as f:
            f.write(data_str)



    def run(self):
        #1.url补全
        for i in range(1):
            # 使用遍历，实现分页功能 其中+要为str类型，所以要进行转换
            url = self.url + str(i) + '.html'
            print(url)
            #2.发送请求
            # 这里不需要self.data_list 并不是全部都得改
            data = self.get_response_url(url)
            # print(data)

            #3.解析 不需要再给变量了
            self.get_response_xpath(data)

        # 4.保存
        self.save_get_response_xpath()

Crawl_fisrt_Bitebi().run()
import requests
from lxml import etree
import re
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


#类插入一个object
class lagouwangSpider(object):
    #创建实例
    def __init__(self):
        #chromedriver.exe的路基所在
        driver_path = r'E:\carlow\Chromedriver\chromedriver.exe'
        #把路径导进去 创建全局的self.driver
        self.driver = webdriver.Chrome(executable_path=driver_path)
        # 首先使用浏览器模仿操作 可以让ajax代码出现在driver.pag_source 所以更容易爬取网页 不容易被发现
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        #创建全局列表
        self.list = []
    def run(self):
        #driver请求url得到数据
        self.driver.get(self.url)
        #抓取网页数据
        response = self.driver.page_source
        #等待网页加载完后再去url
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//a[@class='position_link']/@href"))
        )
        #调用函数 返回值给etree_data(url)
        self.etree_data(response)


    def etree_data(self,response):
        #使用etree解析数据
        etree_data = etree.HTML(response)
        #爬取页数 使用死循环 然后给一个条件后 停止死循环
        while True:
            #抓取网页中所有的js中的请求职业信息详情页的url
            xpath_data = etree_data.xpath('//a[@class="position_link"]/@href')
            #遍历整个页面的url 将url返回给request_url()中处理  一条条的处理
            for position in xpath_data:
                self.request_url(position)
                # print(position)
                #设定沉睡时间
                time.sleep(1)
            # 抓取下一页的按钮
            btn_click = self.driver.find_element_by_xpath('//span[@action="next"]')
            #这里使用条件将死循环结束 如果class属性里有这个值 那么就停下来
            if 'pager_next_disabled' in btn_click.get_attribute('class'):
                break
            #否则运行
            else:
                #点击事件
                btn_click.click()
            time.sleep(10)
            print(xpath_data)


    def request_url(self,url):
        #切换窗口运行
        self.driver.execute_script("window.open('%s')"%url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        # print(self.driver.current_url)
        # self.driver.get(url)
        response = self.driver.page_source

        etree_data = etree.HTML(response)
        self.xpath_data(etree_data)

        #关闭当前页面
        self.driver.close()
        # #然后切换回首页
        self.driver.switch_to.window(self.driver.window_handles[0])


    def xpath_data(self,etree_data):
        # print(response)

        name_data = etree_data.xpath('//span[@class="name"]/text()')[0]
        #其中strip()是减去左右的空格
        salary_data = etree_data.xpath('//span[@class="salary"]/text()')[0].strip()
        city_data = etree_data.xpath('//dd[@class="job_request"]//span/text()')[1].strip()
        #使用正则表达式来替换列表中的空格和特殊符号  re.sub()
        city_data = re.sub('[\s/]', "", city_data)
        experience_data = etree_data.xpath('//dd[@class="job_request"]//span/text()')[2].strip()
        experience_data = re.sub('[\s/]', "", experience_data)
        education_data = etree_data.xpath('//dd[@class="job_request"]//span/text()')[3].strip()
        education_data = re.sub('[\s/]', "", education_data)
        # print(education_data)
        # 列表变字符串
        job_data = "".join(etree_data.xpath('//dd[@class="job-advantage"]//text()'))
        job_data = re.sub('[\s/]', "", job_data)
        # 列表变字符串  "".join(列表放进来)
        desc_data = "".join(etree_data.xpath('//dd[@class="job_bt"]//text()')).strip()
        desc_data = re.sub('[\s/]', "", desc_data)
        company_data = "".join(etree_data.xpath('//em[@class="fl-cn"]/text()'))
        company_data = re.sub('[\s/]', "", company_data)
        print(company_data)
        dict_data = {
            company_data:'招聘公司',
            name_data :'职位名称',
            salary_data : '工资',
            city_data : '城市',
            experience_data : '工作经验',
            education_data : '教育信息',
            job_data : '职位诱惑',
            desc_data : '职位描述'

        }
        print(dict_data)
        print('='*40)
        self.list.append(dict_data)


        pass
        # json_file = json.dump(list_data,open('拉勾网python职业信息.json','w',encoding='utf-8'))
                # print(dict_data)


if __name__ == '__main__':
    source = lagouwangSpider()
    source.run()


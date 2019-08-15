# -*- coding: utf-8 -*-
import scrapy
#一般有图形验证码 使用保存本地路径
from urllib import request
from PIL import Image

class QcwyLoginSpider(scrapy.Spider):
    name = 'qcwy_login'
    allowed_domains = ['login.51job.com']
    start_urls = ['http://login.51job.com/']
    base_url = 'https://login.51job.com/login.php?lang=c'
    post_url = 'https://login.51job.com/login.php?lang=c&url=https%3A%2F%2Fi.51job.com%2Fuserset%2Fmy_51job.php'
    url = 'https://i.51job.com/userset/my_51job.php'


    def parse(self, response):
        data = {
            'lang': 'c',
            'action': 'save',
            'from_domain': 'i',
            'loginname': '18802544885',
            'password': 'as10130503',
            # 'verifycode': '9ays',
                'isread': 'on'
        }

        #得到img的url
        img_url = response.xpath('//img[@id="verifyPic_img"]/@src').get()
        if img_url:
            #因为input_verification(self,img_url)返回的是一个 verification_img    所以verification_img = self.input_verification(img_url)
            verification_img = self.input_verification(img_url)
            print(verification_img)
            #添加字典内容
            data['verifycode'] = verification_img
            #都要写回调函数
            yield scrapy.FormRequest(url=self.post_url, formdata=data, callback=self.login_data)
        else:

            yield scrapy.FormRequest(url=self.post_url,formdata=data,callback=self.login_data)

    def login_data(self,response):

        #response.url可以提取其中的url  可以用来验证是否是请求的url
        if response.url == self.url:
            #这里可以写登录以后的操作
            print('登录成功')

        else:
            print("登录失败")

    def input_verification(self,img_url):
        print(img_url)
        # 然后保存本地
        request.urlretrieve(img_url, r'E:\crawl\qcwy/' + 'verifycode.png')
        # 打开img
        img = Image.open('verifycode.png')
        # 将img打开
        img.show()
        verification_img = input('请输入验证码:')
        return verification_img




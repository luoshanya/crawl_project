import requests
from lxml import etree
import re
import os
from urllib import request
from queue import Queue
import threading

class Product(threading.Thread):
    # 这里开始构建函数 传参 所有参数*args **kwargs
    def __init__(self,img_url_queue,img_download_queue,*args,**kwargs):
        super(Product, self).__init__(*args,**kwargs)
        #设置类部变量 以便后面调用
        self.img_url_queue = img_url_queue
        self.img_download_queue = img_download_queue
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

    def run(self):
        #多线程一般都会使用死循环
        while True:
            #这里使用了安全队列的方法 在里面线程不用加锁 因为队列是安全的
            #这里if self.img_url_queue.empty() 代表如果url管道里的数据为空了 那就退出循环，
            if self.img_url_queue.empty():
                break
            #这里self.img_url_queue.get() 是为了拿到列队里的数据
            url = self.img_url_queue.get()
            self.parse_pgk(url)
    def parse_pgk(self,url):

        #第一种请求方法可以写content的写法
        # response = requests.get(url,headers=headers).content.decode('utf-8')
        #第二种方法
        response = requests.get(url,headers=self.headers).text

        #解析数据
        etree_data = etree.HTML(response)

        #去除属性条件，可以写！=
        xpath_data = etree_data.xpath('//div[@class="random_picture"]//img[@class!="gif"]')
        # print(xpath_data)
        for i in xpath_data:
            picture_url = i.get('data-original')
            # print(picture)
            #获取属性内容可以直接使用get('')
            alt = i.get('alt')
            # print(alt)
            # 正则表达式换符号
            alt = re.sub(r'[?？，。, .!！]','',alt)
            # print(alt)
            #使用os模块 分割文本 其中的文件名后缀也可以分割  ('https://ws4.sinaimg.cn/bmiddle/9150e4e5gy1g0s9yvo94gj20240273yf', '.jpg')
            picture_suffix = os.path.splitext(picture_url)[1]

            picture_name = alt + picture_suffix
            # print(picture_name)
            #其中使用urllib.request.urlretrieve(url,fiiename,文件名)   filename 需要使用r'下载文件路径'才行
            # request.urlretrieve(picture_url,r'E:\crawl\imgs\fuck/'+picture_name)

            #把下载的url和图片名称放进下载队列中 ，让消费者下载    这里放进的是元组
            self.img_download_queue.put((picture_url,picture_name))

class Download_img(threading.Thread):
    def __init__(self,img_url_queue,img_download_queue,*args,**kwargs):
        super(Download_img, self).__init__(*args,**kwargs)
        self.img_url_queue = img_url_queue
        self.img_download_queue = img_download_queue

    def run(self):
        while True:
            #在下载队列里 要不就是url队列空了 循环退出 要不就是下载完了就退出 两个条件缺一不可 所以用and
            if self.img_url_queue.empty() and self.img_download_queue.empty():
                break

            #拿到队列的url下载 再已经放到下载队列中元组的数据 再将其匹配到新的变量中
            picture_url,picture_name = self.img_download_queue.get()

            #拿到url后下载 传输到本地文件中r'文件下载位置' 然后在添加名字
            request.urlretrieve(picture_url,r'E:\crawl\imgs\fuck/'+picture_name)
            print(picture_name,'下载完成')


def main():
    img_url_queue = Queue(100)
    img_download_queue = Queue(1000)
    for i in range(1,100):
        #设定url
        url = 'http://www.doutula.com/photo/list/?page=%d'% i
        #将url放进queue队列中
        img_url_queue.put(url)
        #只循环一次

    for i in range(5):
        #进行传参  把数据传进去
        t = Product(img_url_queue,img_download_queue)
        t.start()
    for i in range(5):
        t = Download_img(img_url_queue,img_download_queue)
        t.start()

if __name__ == '__main__':
    main()
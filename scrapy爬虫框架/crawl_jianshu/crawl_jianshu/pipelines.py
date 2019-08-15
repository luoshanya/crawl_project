# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors
# class CrawlJianshuPipeline(object):
#     def __init__(self):
#         #设置数据库参数  登录数据库
#         dbparams = {
#             'host' : '127.0.0.1',
#             'port' : 3306,
#             'db' : 'crawl',
#             'user' : 'root',
#             'password' : '10130503',
#             'charset' : 'utf8'
#
#         }
#         #建立mysql的链接  然后导入参数 **dbparams **代表导入全部 而且换格式  例host = '127.0.0.1'
#         self.conn = pymysql.connect(**dbparams)
#         #建立游标 例如开始事务
#         self.cursor = self.conn.cursor()
#         # 这里设置全局的参数 然后弄一个装饰器 创建一个功能放进self.sql
#         self._sql = None
#
#     def process_item(self, item, spider):
#         #开始将数据添加进数据库 self.cursor.execute()里面只能添加两个参数，所以一个为装饰器，另一个就是一个列表(数据)
#         self.cursor.execute(self.sql,(item['title'],item['content'],item['author'],item['avatar'],item['pub_time'],item['article_id'],item['origin_url']))
#         self.conn.commit()
#         return item
#
#     #装饰器@property 例如一个def __init__ 就是可以直接使用self.sql 使用里面的功能
#     @property
#     def sql(self):
#         # 如果不是空  那么就开始下面的命令
#         if not self._sql:
#             #对数据库的添加 弄一个装饰器 其中 id不设置 那么就是可以写入一个null 其他的还没输入就可以先弄一个占位符%s
#             self._sql = """
#                 insert into jianshu_article(id,title,content,author,avatar,pub_time,article_id,origin_url) values (null,%s,%s,%s,%s,%s,%s,%s)
#             """
#             return self._sql
#         return self._sql


#异步下载
class JianshuTwistedPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'db': 'crawl',
            'user': 'root',
            'password': '10130503',
            'charset': 'utf8',
            'cursorclass' : cursors.DictCursor
        }
        self.adbapi = adbapi.ConnectionPool('pymysql',**dbparams)
        self._sql = None

    #装饰器是专门定义一个属性 然后直接使用
    @property
    def sql(self):
        # 如果不是空  那么就开始下面的命令
        if not self._sql:
            # 对数据库的添加 弄一个装饰器 其中 id不设置 那么就是可以写入一个null 其他的还没输入就可以先弄一个占位符%s
            self._sql = """
                    insert into jianshu_article(id,title,content,author,avatar,pub_time,article_id,origin_url) values(null,%s,%s,%s,%s,%s,%s,%s)
                """
            return self._sql
        return self._sql


    #函数一定要写对：process_item()
    def process_item(self,item,spider):
        #返回一个对象
        error = self.adbapi.runInteraction(self.insert_item,item)
        #查看对象的处理错误的命令
        error.addErrback(self.error_item,item,spider)

    #这里返回一个cursor
    def insert_item(self,cursor,item):
        #返回的cursor中对数据库开始增加数据
        cursor.execute(self.sql,(item['title'],item['content'],item['author'],item['avatar'],item['pub_time'],item['article_id'],item['origin_url']))
        return item

    #处理错误的函数
    def error_item(self,error,item,spider):
        print('='*30+'error'+'error')
        print(error)
        print('=' * 30 + 'error' + 'error')

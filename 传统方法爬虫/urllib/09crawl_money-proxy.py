import urllib.request


#付费的代理发送
#1.用户名密码（带着）
#通过验证的处理器来发送

def money_proxy_use():
    # #1.代理ip
    # money_proxy_use = {
    #     "http":"username:pwd@192.168.12.11:80"
    # }
    # #2.创建处理器  代理使用ProxyHandler
    # #出现这个错误：TypeError: '>' not supported between instances of 'dict' and 'int'
    # #是因为urllib.request后面写错了
    # opener_handler = urllib.request.ProxyHandler(money_proxy_use)
    # #3.创建opener
    # opener = urllib.request.build_opener(opener_handler)
    #
    # opener.open("http://www.baidu.com")
    # # print(data)

    #第二种方式发送付费的IP地址
    user_name = "xiaoming"
    pwd = "123456"
    proxy_money = "123.158.63.130.8888"
    #2创建密码管理器，添加用户名和密码
    password_manager = urllib.request.HTTPBasicAuthHandler()
    #uri定位 uri>url
    #url 资源定位符
    password_manager.add_password(None,proxy_money,user_name,pwd)
    #3.创建可以验证代理的处理器
    handler_password = urllib.request.ProxyBasicAuthHandler(password_manager)
    # 根据处理器创建opener
    opener = urllib.request.build_opener(handler_password)
    response = opener.open("http://www.baidu.com").read()
    print(response)
money_proxy_use()

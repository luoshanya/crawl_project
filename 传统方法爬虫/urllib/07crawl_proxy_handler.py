import urllib.request

def Create_proxy_handler():
    url = "https://211.66.88.48"
    #导入代理IP地址
    proxy = {
        #免费的写法
        #官方的写法："http":"http://180.119.68.194:9999")
        #简单的写法：
        "http":"180.119.68.194:9999"
        #付费写法："http":"用户名":密码123@IP地址
    }
    #创建代理IP处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)
    #创建自己的opener
    opener_handler = urllib.request.build_opener(proxy_handler)
    #拿着代理IP去发送请求
    data = opener_handler.open(url).read()

    print(data)
Create_proxy_handler()



import urllib.request


def handle_opener():
    url = "https://www.cnblogs.com/zrmw/p/9332801.html"
    #系统的urlopen并没有添加代理的功能，所以需要我们自定义这个功能
    #安全 套接层 ssl第三方的CA数字证书
    #urlopen为什么可以请求数据 handler处理器
    #自己的opener请求数据
    # urllib.request.urlopen()
    #HTTPHandler不能添加代理

    handler = urllib.request.HTTPHandler()
    #创建自己的opener
    handler_opener = urllib.request.build_opener(handler)
    # 创建自己的opener调用open方法请求数据
    response = handler_opener.open(url)

    data = response.read()

    print(response)
    print(data)
handle_opener()
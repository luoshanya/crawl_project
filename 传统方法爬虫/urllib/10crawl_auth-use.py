import urllib.request


def crawl_nei_network():
    user_name = "admin"
    pwd = "admin123"
    nei_network = "http://211.66.88.48"

    #创建密码管理器
    password_maneger = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_maneger.add_password(None,nei_network,user_name,pwd)
    #创建对应的处理器
    handler_password = urllib.request.ProxyBasicAuthHandler(password_maneger)
    opener = urllib.request.build_opener(handler_password)

    #进行验证
    urllib.request.HTTPBasicAuthHandler(password_maneger)

    response = opener.open(nei_network).read()
    print(response)
crawl_nei_network()
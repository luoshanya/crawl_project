import urllib.request


def user_proxy():
    proxy_list = [
        {"http":"171.12.115.99:9999"},
        {"http":"180.119.68.19:9999"},
        {"http":"114.230.69.231:9999"},
        {"http":"115.196.51.161:9000"}
    ]
    #使用遍历
    for proxy in proxy_list:
        print(proxy)
        #创建遍历的
        proxy_handler = urllib.request.HTTPHandler(proxy)
        opener = urllib.request.build_opener(proxy_handler)

        try:
            opener.open("http://211.66.88.48",timeout=1)
            print("haha")

        except Exception as e:
            print(e)
user_proxy()



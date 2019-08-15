import urllib.request


def request_header():
    url = "http://www.baidu.com"
    #创建请求对象
    request = urllib.request.Request(url)

    response = urllib.request.urlopen(request)
    print(response)
    data = response.read().decode('utf-8')

    # 响应头
    # print(response.headers)
    # 获取请求头信息
    request_headers = response.headers
    print(request_headers)
    with open("04crawl.html","w",encoding="utf-8")as f:
        f.write(data)
request_header()

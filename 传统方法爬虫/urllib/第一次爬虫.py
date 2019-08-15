import urllib.request


def crawl_first():
    url = "http://www.baidu.com"
    # http请求
    response = urllib.request.urlopen(url)
    # 读取的内容是bytes类型
    data = response.read()
    # 将读取的文件转换为字符串类型
    Str_data = data.decode("utf-8")
    # 将读取的文件放入文件夹
    with open("first_crawl.html","w",encoding="utf-8")as f:
        f.write(Str_data)
    print(Str_data)
    # 将字符串转换为bytes
    str_name = 'baidu'
    str_bytes = str_name.encode('utf-8')
    # python爬去回来的类型：str bytes
    # 如果爬取回来的是bytes类型：但是你写入的时候需要字符串 就要使用decode("utf-8")
    # 如果爬取回来的是str类型：但是你要写入的是bytes类型 encode（"utf-8")
    
crawl_first()
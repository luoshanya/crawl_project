import urllib.request
import urllib.parse
import string

def get_method_params():
    url = "http://www.baidu.com/s?wd="
    # 拼接字符串（汉字）
    name = '美女'
    final_url = url + name
    print(final_url)
    # 代码发送请求
    # 网址包含了汉字；ASCII是没有汉字的；需要URL转译
    # 将包含汉字的网址进行转译
    encoding_new_title = urllib.parse.quote(final_url,safe=string.printable)
    # 代码发送网络请求
    response = urllib.request.urlopen(encoding_new_title)
    data = response.read()

    #mac电脑的解码方式是utf-8
    #Windows电脑的解码方式是gbk
    str_data = data.decode("utf-8")
    # 保存到本地
    with open("02crawl.html","w",encoding="utf-8") as f:
        f.write(str_data)
    # UnicodeEncodeError:'ascii'codec can't encode
    # characters in position 10-11:ordinat not in range(128)
    # python:是解释性语言，解释器只支持ascii 0-127
    # 不支持中文
    print(str_data)
get_method_params()
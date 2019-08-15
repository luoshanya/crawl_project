import urllib.request
import urllib.parse
import string

def get_params():
    url = "http://www.baidu.com/s?"
    params = {
        "wd":"中文",
        "value":"abc",
        "new":"b"
    }
    # 字典的话需要用这一段命令
    str_params = urllib.parse.urlencode(params)
    start_params = url + str_params
    # 将带有中文的URL转译成计算机可以识别的URL
    final_params = urllib.parse.quote(start_params,safe=string.printable)
    response = urllib.request.urlopen(final_params)
    data = response.read()
    str_data = data.decode('utf-8')
    # with open("03crawl.html","w",encoding="utf-8") as f:
    #     f.write(data)
    print(str_data)
get_params()

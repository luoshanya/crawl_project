import urllib.request
import random


def agent_baidu():
    url = "https://www.cnblogs.com/zrmw/p/9332801.html"
    agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"
    ]
    #这里需要的是[]而不是{}
    #每次请求的浏览器都是不一样的
    random_try = random.choice(agent_list)

    request = urllib.request.Request(url)
    #这里是请求头header而不是handler
    #增加对应的请求头信息（user_agent）
    request.add_header("User-Agent",random_try)
    response = urllib.request.urlopen(request)
    print(response)
    print(request.get_header("User-agent"))
agent_baidu()

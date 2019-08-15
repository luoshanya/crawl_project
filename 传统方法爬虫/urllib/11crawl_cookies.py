import urllib.request
from urllib import parse
from http import cookiejar
import ssl
#1.代码登录
def cookies_crawl():
    #2.登录的网址
    login_url = "https://www.yaozh.com/login/"
    #3.登录的数据
    login_form_data = {
        "username": "zhukelin",
        "pwd": "as751286012",
        "formhash": "6E1A90D3A4",
        "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"
    }

    #4.发送登录请求POST
    cook_jar = cookiejar.CookieJar()
    #定义有添加的 cook 功能的处理器
    cook_handler = urllib.request.HTTPCookieProcessor(cook_jar)
    #根据处理器创建opener
    opener = urllib.request.build_opener(cook_handler)

    #带参数的 发送请求头
    #添加请求头
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    # 出现ssl错误
    ssl._create_default_https_context = ssl._create_unverified_context
    str_data = urllib.parse.urlencode(login_form_data).encode('utf-8')
    login_request = urllib.request.Request(login_url,headers=header,data=str_data)
    #如果登录成功，cookjar自动保存cookie
    opener.open(login_request)

    #代码带着cookie去访问
    center_url = 'https://www.yaozh.com/member/'
    center_data = urllib.request.Request(center_url,headers=header)
    response = opener.open(center_data).read().decode("utf-8")
    with open("11crawl_cookie.html","w",encoding='utf-8')as f:
        f.write(response)
cookies_crawl()
# 利用cookies登录马蜂窝

import requests
from lxml import etree
try:
    import cookielib
except:
    from http import cookiejar as cookielib

session = requests.Session()
# phone_number = '13521093039'
# password = 'pro123,./'
# data = {'passport': phone_number, 'password': password}
data = {}
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
logined_url = 'https://passport.mafengwo.cn/login/'
# response = requests.get(logined_url, headers=header)
# print(response.status_code)
#
# tree = etree.HTML(response.text)
#
# friends = tree.xpath('//div[@class="name"]/a/text()')
# print(friends)
# cookies = session.cookies
session.cookies = cookielib.LWPCookieJar(filename='cookies')

try:
    session.cookies.load(ignore_discard=True)

except:
    print("Cookies加载不成功!")
    data['passport'] = input('请输入你的账号:')
    data['password'] = input('请输入你的密码:')
    # print(data)

def yanzheng_login():
    """
    验证是否登录成功 检查状态码
    :return:
    """
    #allow_redirects=False#设置这个属性为False则是不允许重定向，反之可以重定向
    url = 'http://www.mafengwo.cn/u/63280520.html'
    login_status_code = requests.get(url,headers=headers, allow_redirects=False).status_code
    if login_status_code == 200:
        return True
    else:
        return False


def login_data():
    """
    这里是添加data from表单的数据 进行登录但是有的网站没有 有的有更多的data信息 例如验证码
    :return:
    """
    pass

# def login_success():
#     url =

def login():
    print(data)
    url = 'http://www.mafengwo.cn/u/63280520.html'
    login_response = session.post(url=logined_url,headers=headers,data=data)
    # print(login_response.text)
    response = session.get(url,headers=headers)
    etree_data = etree.HTML(response.text)
    xpath_data = etree_data.xpath('//div[contains(@class,"MProfile")]/@data-intro')
    print(xpath_data)
    session.cookies.save()

if __name__ == '__main__':
    if yanzheng_login():
        print('登录成功!')

    else:
        # pass
        login()
# r = session.post("https://passport.mafengwo.cn/login/", headers=header, data=data)
# print(r.url)
# cookies = session.cookies
# print(cookies)
# print(cookies.get_dict())

# print(r.status_code)
# # print(r.text)
#

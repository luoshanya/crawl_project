import requests


from lxml import etree


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

session = requests.Session()
login_url = 'http://www.cnnfund.com/login.aspx?action=login&from='
data = {
    'username': 'zhukelin',
    'password': '10130503'
}
cookies = session.cookies
response_login = session.post(login_url,headers=headers,cookies=cookies,data=data)
print(cookies)

base_url = 'http://www.cnnfund.com/Notification.aspx?page={}'
for i in range(1, 2):
    urls = base_url.format(i)

    response = requests.get(urls,headers=headers,cookies=cookies).text
    # print(response)



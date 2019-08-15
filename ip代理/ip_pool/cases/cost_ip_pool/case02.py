# 复习requests是如何使用代理的

import requests

proxy = {
    "http": "111.177.162.57:9999",
    "https": "171.41.80.191:9999"
}
header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

url = 'https://www.baidu.com'
response = requests.get(url, proxies=proxy, headers=header, timeout=10)

print(response.status_code)
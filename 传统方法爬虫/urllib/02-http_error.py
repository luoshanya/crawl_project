
# urlib.request  提示错误 HTTPError UrlError
"""
     raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
    
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found

"""

import urllib.request


url = 'https://blog.csdn.net/zjsxxzh/article/details/110'

url = 'https://affdsfsfsdfd.cn'

try:
    response = urllib.request.urlopen(url)

except urllib.request.HTTPError as error:
    print(error.code)


except urllib.request.URLError as error:
    print(error)



import requests

url = "http://www.baidu.com"
response = requests.get(url)

#content属性 返回的类型是bytes
data = response.content.decode("utf-8")
#text属性 返回的类型是文本str
# data = response.text
print(type(data))
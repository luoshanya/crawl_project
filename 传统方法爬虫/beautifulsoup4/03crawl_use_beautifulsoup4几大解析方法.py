from bs4 import BeautifulSoup
import json
#这里是引入Beautifulsoup 不是beautifulsoup4
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story"><!--...--></p>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>


"""

#转类型  :<class 'bs4.BeautifulSoup'>
#这里需要添加lxml声明 不然会出现警告  UserWarning: No parser was explicitly specified,
soup = BeautifulSoup(html_doc,'lxml')

#find--返回符合查询条件的 是第一个标签
# 根据标签名查询
result = soup.find(name='a')
#根据属性查询 需要将属性转换字典类型
result = soup.find(attrs={"class":"sister"})
#也可以一起查询  只可以查询本标签内的数据 不可以跨  例： name='a',a里面的数据  name='a',换p标签之后显示none
result = soup.find(
    name='a',
    attrs={"class":"sister"}

)


#find_all 查询所有的数据
# result = soup.find_all(name='a',limit=1)     结果：[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

#result = soup.find_all(name='a',limit=1)[0]   结果：<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>  就是find()
result = soup.find_all(name='a',limit=1)
result = soup.find_all(attrs={"class":"sister"},limit=1)
#也可以组合用


#select_one  css选择器 需要使用.sister #id
result = soup.select_one('a')
result = soup.select_one('.sister')

#selet css选择器    limit=1代表限制 只能一次
result = soup.select('.sister',limit=1)
#id选择器
result = soup.select('#link1')
#后代选择器
result = soup.select('head title')
#组选择器 标签，.类
result = soup.select('title,.title')
#属性选择器  将需要找的属性直接写出来就行
result = soup.select('a[id="link1"]')
result = soup.select('a[class="sister"]')



result = soup.select('title,a,.title')

# data = json.dumps(result)
# print(data)
# dicts = {}
for i in result:
    print(type(i))
#     dicts.append(dicts)
# print(dicts)
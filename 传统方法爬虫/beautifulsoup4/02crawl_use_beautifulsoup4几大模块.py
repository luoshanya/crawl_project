from bs4 import BeautifulSoup
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
# print(type(soup))


#内容属于tag类型  这样只能查询到第一条而不是全部
result = soup.a
result = soup.p


#抓取文本使用string 内容属于Navigablestring   <class 'bs4.element.NavigableString'>
result = soup.a.string

#抓取url或者属性 内容属性为str   <class 'str'>
result = soup.a['href']

#注释的内容string 类型是comment    <class 'bs4.element.Comment'>
result=soup.p.string

print(type(result))
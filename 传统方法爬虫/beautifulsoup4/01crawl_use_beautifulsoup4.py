from bs4 import BeautifulSoup
#这里是引入Beautifulsoup 不是beautifulsoup4
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

#转类型
#这里需要添加lxml声明 不然会出现警告  UserWarning: No parser was explicitly specified,
soup = BeautifulSoup(html_doc,'lxml')
#bs4会自动补全HTML信息
result = soup.prettify()
print(result)
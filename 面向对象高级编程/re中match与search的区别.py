__author__ = 'zhukelin'
__date__ = '2019/4/17 0017 下午 3:37'

a = "helloworld helloworld"
b = 'hello'
c = 'world'

import re
# search扫描整个字符串
print(re.search(c,a))
print(re.search(c,a).group())

# match：只在字符串的开始位置进行匹配
print(re.match(b,a))
print(re.match(b,a).group())

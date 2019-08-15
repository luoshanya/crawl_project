__author__ = 'zhukelin'
__date__ = '2019/4/17 0017 下午 3:15'


a = "Hello Welcome my home"
b = a.split("[ m]")
print(b)


import re
# re可以进行多个要求进行拆分 但是上面的普通split不行
c = re.split("[ m]",a)
print(c)
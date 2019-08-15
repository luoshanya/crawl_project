import re

#纯数字的正则 \d 0-9之间的一个数
#^ $组合代表从头到尾 +代表至少一次
pattern = re.compile('^\d+$')

#其中不能存在其他字符（不是数字），不然报错
one = '1234'
#匹配判断方法
#match方法 是否匹配成功 从头匹配一次
result = pattern.match(one)
# 需要写.group()才会显示数字
print(result.group())
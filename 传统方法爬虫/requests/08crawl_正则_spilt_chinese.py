import re


one = 'asbsnsmsj'
pattern = re.compile('s')

result = pattern.split(one)
# print(result)

#匹配中文
two = '<a href="https://blog.csdn.net/u011379545/article/details/38083849" target="_blank">EL表达式中使用三目运算符,年后</a>'

#python中 匹配中间[a-z] unicode的范围： [ \u4e00-\u9fa5]   * + ？都是量词

pattern = re.compile('[\u4e00-\u9fa5]+')
#查询所有符合中文的字符出来，使用findall
result = pattern.findall(two)

print(result)

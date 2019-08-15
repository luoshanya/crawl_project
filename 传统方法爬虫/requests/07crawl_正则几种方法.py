import re

#正则使用re

one = 'abc123'

pattern = re.compile('\d+')

#match方法 从头开始匹配，只匹配一次,但如果第一个不是数字就会报错
result = pattern.match(one)
#结果：<re.Match object; span=(0, 3), match='123'>

#使用search方法 从任意位置开始匹配 只匹配一次
result = pattern.search(one)
#结果:<re.Match object; span=(0, 3), match='123'>

#findall方法 查找符合正则的内容 --list
result = pattern.findall(one)
#结果:['123']

#sub方法 替换字符串
result = pattern.sub('#',one)
#结果：abc#

#split拆分   字符中间需要有空格
one = 'abc 123'
pattern = re.compile(' ')
result = pattern.split(one)



print(result)
import re

one = 'ababababjjjjn11111222n'
two = 'a\b'
#贪婪模式 从头匹配到尾 默认
# pattern = re.compile('a(.*)n')

#非贪婪模式 只中断一次 只选择第一个元素开始匹配
# pattern = re.compile('a(.*?)n')
# print(pattern.findall(one))

#有r与没r的差别：有r：['a']   没有r：['a\x08']
# pattern = re.compile('a\b')
# test_pattern = pattern.findall(two)
# print(test_pattern)


# . 除了换行符号\n之外的匹配
# one = """
#     mmmmmmssslakoj
#     ndj1234445M
# """
#这段代码表示不能匹配换行\n之后的字符
# pattern = re.compile('m(.*)m')

#如果需要匹配换行\n后面的字符，name代码需要写成   re.S忽略换行  re.I忽略大小写
# pattern = re.compile('m(.*)m',re.S | re.I)
# result = pattern.findall(one)
# print(result)
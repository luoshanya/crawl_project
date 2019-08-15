__author__ = 'zhukelin'
__date__ = '2019/4/17 0017 下午 2:50'

def square(x):
    return x**2

print(square(10))

# 使用匿名函数 lambda匿名函数就像def square(x):  下面的x**2就是return的结果
a = lambda x:x**2
print(a(10))

# list_data =[1,2,3,4,5,6]
# a = list(map(lambda x:x**2,list_data))
# print(a)
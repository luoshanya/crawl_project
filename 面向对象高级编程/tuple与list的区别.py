__author__ = 'zhukelin'
__date__ = '2019/4/17 0017 下午 3:05'

tuple_a = (1,2,3,4,5)
list_a = [1,2,3,4,5,6]

# tuple元素不可以修改 不然直接报错  TypeError: 'tuple' object does not support item assignment
# tuple_a[0] = 1
list_a[0] = 10

print(tuple_a)
print(list_a)
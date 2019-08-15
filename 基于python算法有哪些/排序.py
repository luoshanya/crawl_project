__author__ = 'zhukelin'
__date__ = '2019/4/17 0017 下午 6:20'


list_data = [2,3,877,5,1]
# 从小到大排序使用sorted
data = sorted(list_data)
# 从大到小排序使用sorted 然后加参数reverse=True
data01 = sorted(list_data,reverse=True)
# print(data)
# print(data01)

# 这个可以改变原来列表的顺序 上面的不会
list_data.sort(reverse=True)
print(list_data)
# a = 1
# b = a
# a += 1
# print(a)

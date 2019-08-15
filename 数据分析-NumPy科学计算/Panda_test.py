__author__ = 'zhukelin'
__date__ = '2019/4/15 0015 上午 2:13'

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

# import pandas as pd
# 加了一个下标index 1,2,3,4
# obj = Series([4, 7, -5, 3])
# print(obj)

# 自定义的下标
# obj2 = Series([1,4,1514,5484,2,84], index = ["a","b","c","d","e","f"])
# print(obj2["a"])
# result = np.exp(obj2)
# print(result)
# print("a" in obj2)

# 如果数据被存放在一个Python字典中，也可以直接通过这个字典来创建Series
# data = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
# data1 = Series(data)
# 必须数据相同 才可以调换位置  不然显示a   NaN
# index = ['California', 'Ohio', 'Oregon', 'Texas']
# index = ["a","x","c","d"]
# obj = Series(data,index)
# print(obj)

# 找出哪一个是null的数据
# result = pd.isnull(obj)
# 或者使用这个查看不是null的数据
# result = pd.notnull(obj)
# 相加可以确定是哪一个值错误 数据对齐功能将在后面详细讲解。如果你使用过数据库，你可以认为是类似join的操作
# print(result + data1)

# 设置显示名称
# obj.name = "population"
# obj.index.name = "status"
# print(obj)

# DataFrame中的数据是以一个或多个二维块存放的（而不是列表、字典或别的一维数据结构）
# 结果DataFrame会自动加上索引（跟Series一样），且全部列会被有序排列：
# data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
#         'year': [2000, 2001, 2002, 2001, 2002, 2003],
#         'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
# frame = pd.DataFrame(data)
# print(frame)

# 对于特别大的DataFrame，head方法会选取前五行：
# header = frame.head()
# print(header)

# 如果传入的列在数据中找不到，就会在结果中产生缺失值：
# frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],index=['one', 'two', 'three', 'four', 'five', 'six'])
# print(frame2.columns)
# 结果 Index(['year', 'state', 'pop', 'debt'], dtype='object')

data = Series(['apple','banana','pair'],index=[0,2,4])
print(data)
data1 = data.reindex(range(6),method="ffill")
print(data1)
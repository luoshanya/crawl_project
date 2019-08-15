import numpy as np
import matplotlib.pyplot as plt


#设置随机数
# random_data = np.random.rand(2,3)
# print(random_data)
# print(random_data*10)

#返回源随机数头(2,3) 与上面相同
# print(random_data.shape)

#返回浮点数
# print(random_data.dtype)

#快速创建数组  numpy.ndarray 类型
# data = [2,4,6,7,8]
#
# data_ndarray = np.array(data)
# print(type(data_ndarray))

#多元数组也一样 转数组
# data = [[1,2,3,4],[5,6,7,8]]
# data_ndarray = np.array(data)
# print(data_ndarray.shape)
# print(data_ndarray.ndim)


# arr = np.array(range(10))
# # 从0开始算
# print(arr[0])

import random
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)
plt.plot(walk[:100])
# 要加plt.show 不然不显示图片
plt.show()
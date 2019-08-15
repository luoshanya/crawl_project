import os

# os.path.dirname(__file__) 这代表查看此文件的当前目录  可以重复使用一直查看当前目录
# print(os.path.dirname(os.path.dirname(__file__)))

#os模块可以进行拼接文件路径
imgs = os.path.join(os.path.dirname(os.path.dirname(__file__)),'imgs')

# 判断文件路径是否存在
path = os.path.exists(imgs)
print(imgs)
if not path:
    os.makedirs(imgs)
else:
    print('文件存在')
#查看当前有没有这个文件夹

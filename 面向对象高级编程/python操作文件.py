__author__ = 'zhukelin'
__date__ = '2019/4/17 0017 下午 6:08'

# 写文件  其中wt代表以写入文本方式进行打开
f = open('test.txt','wt')
# 写入数据
f.write("hello world")
# 忘记关闭就用with open方法
f.close()

# 使用with，追加内容，不用关心文件关闭问题  a代表添加 t文本 以添加文本的方式进行读写
with open('test.txt','at') as f:
    f.write('\nhello wold')


# 读取文件  读取文本read txt 简写rt
with open("test.txt", 'rt') as f:
    print(f.read())
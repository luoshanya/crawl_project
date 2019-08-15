__author__ = 'zhukelin'
__date__ = '2019/4/17 0017 下午 2:35'

# 导入socket模块
import socket

s = socket.socket()

# 连接服务端
s.connect(("127.0.0.1",6666))
# 接收数据
print(s.recv(1204))
s.close()
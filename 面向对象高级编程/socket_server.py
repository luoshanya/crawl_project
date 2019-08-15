__author__ = 'zhukelin'
__date__ = '2019/4/17 0017 下午 2:41'

# 首先导入模块socket
import socket

# 创建socket的对象
s = socket.socket()

# 绑定一个端口和ip
s.bind(("127.0.0.1",6666),)

# 实现监听功能 等待
s.listen(5)

# 写一个死循环 一直等待客户端连接的状态
while True:
    # 取值 确认请求
    c, addr = s.accept()
    print("连接地址:",addr)
    # send传的是字节 所以需要在str前加一个b  因为
    c.send(b"Welcome")
    # 连接成功后关闭
    c.close()
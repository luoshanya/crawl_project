# 多进程，使用Process对象

from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    #进程Process target=函数名  args=参数名
    p_1 = Process(target=f, args=('bob',))
    #开始进程
    p_1.start()
    #载入
    p_1.join()

    p_2 = Process(target=f, args=('alice',))
    p_2.start()
    p_2.join()
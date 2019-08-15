__author__ = 'zhukelin'
__date__ = '2019/4/17 0017 下午 1:58'
# 进程
# from multiprocessing import Process,Pool
#
# def foo(i):
#     print("This is Process",i)
#
#
# if __name__ == '__main__':
#     # 调用多个进程
#     # for i in range(5):
#         # 进程配置方法 与参数
#         # t = Process(target=foo,args=(i,))
#         # t.start()
#     # 进程池的使用
#     p = Pool(5)
#     list = [1,2,3,4,5,6,6,]
#     p.map(foo,list)


# 线程
# import threading
#
# def show(i):
#     print('This is Threading',i)
#
# for i in range(5):
#     # 这里使用i传参 必须在后面加,号 不然报错
#     t = threading.Thread(target=show,args=(i,))
#     t.start()

# 协程  高并发实现模块gevent 不然使用asyncio
import gevent
def foo():
    print("start_foo")
    # 延迟输出后面的语句
    gevent.sleep(2)
    print("end_foo")

# 先执行的代码先执行 不按顺序输出 不用等待
def bar():
    print("start_bar")
    gevent.sleep(0)
    print("end_bar")

# foo()
# bar()
# 调用函数
gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])


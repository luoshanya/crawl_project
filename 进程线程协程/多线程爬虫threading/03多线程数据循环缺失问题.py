import threading

#定义全局变量
VALUE = 0

# 创建线程锁

glock = threading.Lock()

def coding():
    #这里需要表名使用全局变量 global()
    global VALUE

    #开锁
    glock.acquire()

    #循环一百万次时 数据出现错误     因为出现两个线程同时运行的问题 所以需要给线程加锁才可以搞定此问题
    for i in range(100000):
        VALUE += 1
    #关锁
    glock.release()
    print(VALUE)
def main():
    #使用循环来执行线程个数
    for x in range(2):
        t1 = threading.Thread(target=coding)

        t1.start()


if __name__ == '__main__':
    main()
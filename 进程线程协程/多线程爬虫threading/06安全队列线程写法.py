from queue import Queue
import threading
import time


# for i in range(5):
#     t = q.put(i)
# q = Queue(4)
# for i in range(10):
#     q.put(i)
# print(q.get())
def queue(q):
    index = 0
    # 设计死循环
    while True:
        #将数据添加队列
        q.put(index)
        index += 1
        time.sleep(3)


def get_queue(q):
    while True:
        print(q.get())

def main():
    #设置函数调用的变量   Queue(maxsize)
    q = Queue(4)
    #在线程中添加数据 需要使用args=[q]
    t1 = threading.Thread(target=queue,args=[q])
    t2 = threading.Thread(target=get_queue,args=[q])

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
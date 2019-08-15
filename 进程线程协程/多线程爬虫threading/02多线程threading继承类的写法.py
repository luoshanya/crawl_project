import threading
import time


#写一个继承类 继承threading.Thread
class Coding(threading.Thread):
    #这里调用run函数
    def run(self):
        for i in range(3):
            print("正在写代码",threading.current_thread())
            #设置代码延迟时间
            time.sleep(1)

class Download(threading.Thread):
    def run(self):
        for i in range(3):
            print("正在下载图片",threading.current_thread())
            time.sleep(1)


def main():

    #这里直接调用线程类
    t1 = Coding()
    t2 = Download()

    #启动线程类
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
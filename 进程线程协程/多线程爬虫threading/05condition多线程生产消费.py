import threading
#导入随机数 random
import random
#创建全局变量
import time
Money = 1000
gTimes = 0
#创建锁    这个condition是继承了Lock的
gCondition = threading.Condition()

#封装成一个类
class Prodect(threading.Thread):
    def run(self):
        global Money
        global gTimes

        #设定死循环 while True:
        while True:
            money = random.randint(100, 1000)
            #开锁acquire()
            gCondition.acquire()
            if gTimes >= 10:
                gCondition.release()
                break
            gTimes += 1
            Money += money
            #格式输出 s%代表第一个占位 %d代表后面的数据 按顺序输出
            print('%s生产金额%d,余额%d'%(threading.current_thread(),money,Money))
            #唤醒condition.wait()的线程
            gCondition.notify_all()
            # 释放锁
            gCondition.release()
            time.sleep(0.5)

#封装成一个类
class Consume(threading.Thread):
    def run(self):
        #表名使用全局变量
        global Money
        global gTimes


        while True:
            # 设置随机金额random.randint(,)
            consume_money = random.randint(100, 1000)
            #开启锁
            gCondition.acquire()

            #这里需要考虑钱不够的情况   这里不用if是因为用if的话不够安全 这个线程在等待 但是还有其他线程在继续 有可能会影响到数据的完整和安全 所以要使用while
            while Money < consume_money:
                #十次之后就退出
                if gTimes >= 10:
                    #释放锁
                    gCondition.release()
                    #因为一个break只能结束一个while 所以这里需要使用return来退出循环
                    return
                print('%s准备消费%d,余额不足%d'%(threading.current_thread(),consume_money,Money))

                #进行等待 不用死循环 耗cpu
                gCondition.wait()
            #钱的计算必须在后面，不然会出现负数等情况
            Money -= consume_money
            print('%s消费金额%d,余额%d' % (threading.current_thread(), consume_money, Money))
            gCondition.release()


            time.sleep(0.5)

#主函数放在第一行
def main():
    #运行线程的代码
    for i in range(3):
        # 调用类
        t1 = Consume(name="消费者线程")
        # 开启线程
        t1.start()

    for a in range(5):
        # 可以直接调用类
        t2 = Prodect(name="生产者线程")
        #开启线程
        t2.start()

#启动函数

if __name__ == '__main__':
        main()

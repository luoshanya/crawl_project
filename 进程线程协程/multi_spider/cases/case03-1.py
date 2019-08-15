import threadpool
import time

#一般很少使用多线程写爬虫 因为在爬虫过程中 如果有一个爬虫出问题了 那么在这个进程中的所有线程都会停止 所以不建议使用多线程爬虫


def sayhello (a):
    print("hello: "+a)
    time.sleep(2)

def main():
    global result
    seed=["a","b","c"]
    start=time.time()
    task_pool=threadpool.ThreadPool(5)
    requests=threadpool.makeRequests(sayhello,seed)
    for req in requests:
        task_pool.putRequest(req)
    task_pool.wait()
    end=time.time()
    time_m = end-start
    print("time: "+str(time_m))
    start1=time.time()
    for each in seed:
        sayhello(each)
    end1=time.time()
    print("time1: "+str(end1-start1))

if __name__ == '__main__':
    main()
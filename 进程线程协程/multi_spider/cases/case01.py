# 多进程，使用Pool

from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    #进程池 Pool(5)代表有5个进程
    p = Pool(5)
    list = [1,2,3,4,5,6,7,8,9]

    #其中map代表是映射 给列表每一个元素执行一次函数f
    print(p.map(f, list))
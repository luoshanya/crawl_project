__author__ = 'zhukelin'
__date__ = '2019/4/17 0017 下午 8:29'

#0,1不是素数
#除了1和它本身外，不能被其他自然数整除的数

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n-1):
        # 使用除去本身和1 去除于n 如果能余数为0 那么传进来的你就不是素数了 返回False
        if n % i == 0:
            # print(n % i)  如果使这个if有意义但是返回的值什么都没有 那么就return False
            return False
    #
    return True

for i in range(0,100):
    if is_prime(i):
        print(i)
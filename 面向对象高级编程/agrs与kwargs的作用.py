__author__ = 'zhukelin'
__date__ = '2019/4/17 0017 下午 3:21'

# 传入多个参数的时候 使用*args 不然会报错
# def test_args(first,*args):
#     print(first)
#     for v in args:
#         print("args %s"%v)

# args = (2,3,4,5,6)
# 在你不知道有多少个参数传参的时候可以使用*args
# test_args(1,2,3,4,5,6,7)

#**kwargs
def test_kwagrs(fisrt,*args,**kwargs):
    print(fisrt)
    for i in args:
        print("args %s"%i)
    # 如果是键值对 那么就有items()方法
    for k,v in kwargs.items():
        # 那么就有两个参数了 两个参数以上必须用括号 然后结合
        print("kwargs ",(k,v))
# *args = (1,23,4,5,6)
# **kwargs(k=2,b=3,m=5)
test_kwagrs(1,23,4,5,6,k=2,b=3,m=5)
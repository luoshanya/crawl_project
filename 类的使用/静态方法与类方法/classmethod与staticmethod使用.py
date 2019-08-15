class test():
    def __init__(self):
        pass

    def putong_method(self):
        print('这是普通方法')


    @classmethod
    def classmothed(cls):
        print('这是类方法')

    @staticmethod
    def staticmethod():
        print('这是静态方法')

#普通方法时 对象调用方法
test_data = test()
test_data.putong_method()

#与普通方法不一样的是 这是使用类调用方法
test.classmothed()

test.staticmethod()

#相同点：对于所有的方法而言，均属于类（非对象）中，所以，在内存中也只保存一份。

# 不同点：方法调用者不同、调用方法时自动传入的参数不同。
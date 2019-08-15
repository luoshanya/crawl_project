__author__ = 'zhukelin'
__date__ = '2019/4/17 0017 下午 1:43'

# Animal是父类，相同事物的统称
class Animal(object):
    def run(self):
        print("Animal is runing......")

# Dog类，继承与Animal类 为子类
class Dog(Animal):
    pass

# 创建对象
dog = Dog()
dog.run()

# 多态，子类覆盖父类方法
class Cat(Animal):
    def __init__(self,name):
        #__name是属性
        self.__name = name

    def getName(self):
        print(self.__name)

    # 覆盖的run方法
    def run(self):
        print('cat is running ....')

cat = Cat("zhulkin")
cat.getName()
cat.run()
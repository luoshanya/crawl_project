class Screen(object):
    @property
    def width(self):
        #不能直接写self.width 因为与函数名冲突了
        return self._width

    @width.setter
    def width(self,value):
        if 0 > value:
            raise ValueError("value must be >0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        if 0 > value:
            raise ValueError("value must be >0")
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width

#装饰器使用  直接定义即可 然后调用
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
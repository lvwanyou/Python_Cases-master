#!/usr/bin/python3
import os
import glob
# 类定义
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


class student(People):
    __grade = int(0)

    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.__grade = g

    def speak(self):
        print("{0:2}说: 我{1:2}岁;{2:2}kg;{3:2d}分;".format(self.name, self.age, self.weight, self.__grade))

    def __str__(self):
        pass
s = student('ken', 10, 60, 20)
s.speak()
s.__str__()
print(os.getcwd())
print(dir())
print(glob.glob("*.py"))
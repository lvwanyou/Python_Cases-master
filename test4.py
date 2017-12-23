# #!/usr/bin/python
# # -*- coding:UTF-8 -*-
#
# import sys
# from collections import deque
#
# # stack = [3, 4, 5]
# # stack.append(6)
# # stack.append(7)
# # stack.insert(0, 2)
# # print(stack)
# # stack = deque(stack)
# # print(stack.popleft(), end='')
# # sys.exit()
#
# import sys
# from test3 import test
# from test2 import test2_0
#
# # test()
# # if __name__="__main__":
# # if __name__ == '__main__':
# print("main")
# str = "hello world"
# # print(str)
# # print(repr(str))
# x = 1
# # print(repr(x).ljust(2), repr(x * x).rjust(2), end='')
# # print("%d shi %d"%(1,2))
# str = input("please input:")
# print("what you input is {}".format(str))
# table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# for name, number in table.items():
#     print("{0:10}==>{1:8d}".format(name, number))
# # else:
# # test2_0()
#
#

# 打开一个文件


# f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
#
# # 关闭打开的文件
# f.close()
# g=open("C:/Users/lenovo/Desktop/aaa.txt", "r+")
# str=g.read()
# print(str)
# print(repr(str))
# print(g.tell())
import pickle
import pprint

output = open("C:/Users/lenovo/Desktop/aaa.txt", "wb")
stack = [3, 4, 5]
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
pickle.dump(stack, output)
pickle.dump(table, output, -1)
output.close()

read = open("C:/Users/lenovo/Desktop/aaa.txt", "rb")
data1 = pickle.load(read)
print(data1)
data2=pickle.load(read)
print(data2)
read.close()
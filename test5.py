# /usr/bin/python
from urllib import request

# 从百度读取数据存入aaa.txt中
response = request.urlopen("http://www.baidu.com/")
output = open("C:/Users/lenovo/Desktop/aaa.txt", "w")
output.write(str(response.read()))
output.close()

# 从aaa.txt中存入数据打印到命令行
read = open("C:/Users/lenovo/Desktop/aaa.txt", "r")

for line in read:
    print(line)


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()
print(type(t))
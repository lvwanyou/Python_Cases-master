# -*- coding:utf-8 -*-
# numbers = [12, 13, 14, 15, 16, 17, 18, 19]

# for index in range(len(numbers)):
#     print(numbers[index])

# coding :utf-8


# 找到10到20之间的质数和合数
def isNum():
    for num in range(10, 20):  # range is [10-19]
        for temp in range(2, num):
            if num % temp == 0:
                print('这是个合数 %d ' % num)
                break
            else:
                if temp == num - 1:
                    print('这是个质数 %d' % num)


def temp(handler):
    handler()


if __name__ == "__main__":
    a = 1
    b = 2
    temp(isNum)

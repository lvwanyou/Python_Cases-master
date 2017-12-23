#!/usr/bin/python
# -*- coding:UTF-8 -*-
import sys


def test():
    print('this is test3')


def aaa(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return a
        a, b = b, a + b
        counter += 1


if __name__ == '__main__':
    f = aaa(5)  # f 是一个迭代器，由生成器返回生成
    try:
        print(f, end='')
    except:
        sys.exit()

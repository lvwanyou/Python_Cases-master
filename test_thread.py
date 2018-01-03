#!/usr/bin/python3
import time
import _thread


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 2:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


# 创建两个线程
try:
<<<<<<< HEAD
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 2, ) )
=======
    _thread.start_new_thread(print_time, ("Thread-1", 2,))
    _thread.start_new_thread(print_time, ("Thread-2", 4,))
>>>>>>> 8e07c9099af0b02cccda878810af45c473c103e5
except:
    print("Error: 无法启动线程")

while 1:
    pass

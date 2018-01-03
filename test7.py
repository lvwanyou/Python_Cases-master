#!/usr/bin/python3
from datetime  import date
from test_thread import print_time
now=date.today()
now.strftime("%y/%m/%d")
print_time()
print(now)
birthday=date(1995,9,15)
print((now-birthday).days)
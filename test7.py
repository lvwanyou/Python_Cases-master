#!/usr/bin/python3
from datetime  import date
now=date.today()
now.strftime("%y/%m/%d")
print(now)
birthday=date(1995,9,15)
print((now-birthday).days)
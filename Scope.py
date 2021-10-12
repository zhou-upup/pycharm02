# -*- coding = utf-8 -*-
# @Time : 2021/10/1 9:59
# @Author : 周孝尚
# @File : Scope.py
# @Software : PyCharm
x = 100

def myfunc():
  # global x
  x = 200

myfunc()

print(x)
# -*- coding = utf-8 -*-
# @Time : 2021/10/3 15:55
# @Author : 周孝尚
# @File : ExceptionTest.py
# @Software : PyCharm
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
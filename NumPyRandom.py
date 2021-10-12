# -*- coding = utf-8 -*-
# @Time : 2021/10/5 17:59
# @Author : 周孝尚
# @File : NumPyRandom.py
# @Software : PyCharm
# from numpy import random
#
# x = random.randint(100)
#
# print(x)
from numpy import random

x = random.randint(100, size=(3, 5))

print(x)
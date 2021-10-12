# -*- coding = utf-8 -*-
# @Time : 2021/10/5 17:44
# @Author : 周孝尚
# @File : NumPyFilter.py
# @Software : PyCharm
import numpy as np

arr = np.array([61, 62, 63, 64, 65])

x = [True, False, True, False, True]

newarr = arr[x]

print(newarr)
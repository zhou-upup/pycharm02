# -*- coding = utf-8 -*-
# @Time : 2021/10/5 12:06
# @Author : 周孝尚
# @File : NumPyReshape.py
# @Software : PyCharm
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)
print(newarr.base)
# -*- coding = utf-8 -*-
# @Time : 2021/10/5 16:46
# @Author : 周孝尚
# @File : NumPySplit.py
# @Software : PyCharm
# import numpy as np
#
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
#
# newarr = np.array_split(arr, 3)
#
# print(newarr)
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)
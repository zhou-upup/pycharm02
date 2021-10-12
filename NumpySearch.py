# -*- coding = utf-8 -*-
# @Time : 2021/10/5 17:11
# @Author : 周孝尚
# @File : NumpySearch.py
# @Software : PyCharm
# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 4, 4])
#
# x = np.where(arr == 4)
#
# print(x)
# import numpy as np
#
# arr = np.array([6,1, 7, 8, 9])
#
# x = np.searchsorted(arr, 7)
#
# print(x)
import numpy as np

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)
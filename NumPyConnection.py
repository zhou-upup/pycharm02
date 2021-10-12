# -*- coding = utf-8 -*-
# @Time : 2021/10/5 15:52
# @Author : 周孝尚
# @File : NumPyConnection.py
# @Software : PyCharm
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.concatenate((arr1, arr2))
# print(arr)
# import numpy as np
# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis=0)
# print(arr)
import numpy as np

# arr1 = np.array([1, 2, 3])
# [[1 4]
#  [2 5]
#  [3 6]]
#
# arr2 = np.array([4, 5, 6])
# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
#
#
# arr = np.stack((arr1, arr2), axis=1)
#
# print(arr)
# import numpy as np
#
# arr1 = np.array([1, 2, 3])
#
# arr2 = np.array([4, 5, 6])
#
# arr = np.stack((arr1, arr2), axis=0)
#
# print(arr)
# import numpy as np
#
# arr1 = np.array([1, 2, 3])
#
# arr2 = np.array([4, 5, 6])
#
# arr = np.vstack((arr1, arr2))
#
# print(arr)
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)

# -*- coding = utf-8 -*-
# @Time : 2021/10/9 10:57
# @Author : 周孝尚
# @File : MachineLearingLine.py
# @Software : PyCharm
import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

print(type(stats.linregress(x, y)))

# def myfunc(x):
#   return slope * x + intercept
#
# mymodel = list(map(myfunc, x))
#
# plt.scatter(x, y)
# plt.plot(x, mymodel)
# plt.show()
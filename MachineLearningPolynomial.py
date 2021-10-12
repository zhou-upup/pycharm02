# -*- coding = utf-8 -*-
# @Time : 2021/10/9 11:36
# @Author : 周孝尚
# @File : MachineLearningPolynomial.py
# @Software : PyCharm
import numpy as np
import matplotlib.pyplot as plt

# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
#
# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
#
# myline = numpy.linspace(1, 22, 100)
#
# plt.scatter(x, y)
# plt.plot(myline, mymodel(myline))
# plt.show()
# xxx = np.arange(0, 1000)
# print(xxx)
import numpy as np
import matplotlib.pyplot as plt
#
# xxx = np.arange(0, 1000)  # x值，此时表示弧度
# yyy = np.sin(xxx*np.pi/180)  #函数值，转化成度
# z1 = np.polyfit(xxx, yyy, 7) # 用7次多项式拟合，可改变多项式阶数；
# p1 = np.poly1d(z1) #得到多项式系数，按照阶数从高到低排列
# print(p1)  #显示多项式
import numpy
import matplotlib.pyplot as plt
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
mymodel = numpy.poly1d(numpy.polyfit(x,y,5))
myline = numpy.linspace(1,22,100)
plt.scatter(x,y)
plt.plot(myline,mymodel(myline))
plt.show()
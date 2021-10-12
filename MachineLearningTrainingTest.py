# -*- coding = utf-8 -*-
# @Time : 2021/10/10 11:48
# @Author : 周孝尚
# @File : MachineLearningTrainingTest.py
# @Software : PyCharm
# import numpy
# import matplotlib.pyplot as plt
# numpy.random.seed(2)
#
# x = numpy.random.normal(3, 1, 100)
# y = numpy.random.normal(150, 40, 100) / x
#
# plt.scatter(x, y)
# plt.show()
# # print(type(x))
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
numpy.random.seed(2)
x = numpy.random.normal(3,1,100)
y = numpy.random.normal(150,40,100) / x
# x = numpy.random.normal(3, 1, 100)
# y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x,train_y,4))
myline = numpy.linspace(0,6,100)

plt.scatter(train_x,train_y)
plt.plot(myline,mymodel(myline))
plt.show()
r2 = r2_score(train_y,mymodel(train_x))
r3 = r2_score(test_y,mymodel(test_x))
print(r2)
print(r3)
print(mymodel(1))
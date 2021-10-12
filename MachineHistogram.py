# -*- coding = utf-8 -*-
# @Time : 2021/10/7 12:00
# @Author : 周孝尚
# @File : MachineHistogram.py
# @Software : PyCharm
import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()
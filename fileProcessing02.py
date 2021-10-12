# -*- coding = utf-8 -*-
# @Time : 2021/10/3 17:07
# @Author : 周孝尚
# @File : fileProcessing02.py
# @Software : PyCharm
f = open("demofile.txt", "r")
i = 0
for x in f:
  if i <=1 :
    print(x)
    i += 1
  else:
    break
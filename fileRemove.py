# -*- coding = utf-8 -*-
# @Time : 2021/10/3 17:29
# @Author : 周孝尚
# @File : fileRemove.py
# @Software : PyCharm
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
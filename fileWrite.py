# -*- coding = utf-8 -*-
# @Time : 2021/10/3 17:21
# @Author : 周孝尚
# @File : fileWrite.py
# @Software : PyCharm
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# 追加后，打开并读取该文件：
f = open("demofile2.txt", "r")
print(f.read())
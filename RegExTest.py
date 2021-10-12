# -*- coding = utf-8 -*-
# @Time : 2021/10/2 11:11
# @Author : 周孝尚
# @File : RegExTest.py
# @Software : PyCharm
import re

# txt = "China is a great country"
# x = re.search("^China.*countrqy$", txt)
# print(type(x))
# print(x)
# import re
#
# str = "China is a great country"
# x = re.sub("\s", "9", str, 2)
# print(x)
import re

# str = "China is a great country"
# x = re.search("a", str)
# print(x) # 将打印一个对象
import re

str = "China is a great country"
x = re.search(r"\bC\w+", str)
print(x.span())
print(x.string)
print(x.group())
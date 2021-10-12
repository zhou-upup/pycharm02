# -*- coding = utf-8 -*-
# @Time : 2021/9/30 21:51
# @Author : 周孝尚
# @File : Iterator02.py
# @Software : PyCharm
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 5:
      i = self.a
      self.a += 1
      return i
    else:
      raise StopIteration


x = MyNumbers()
a = iter(x)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# while (next(a) != None):
#   print(next(a))

# -*- coding = utf-8 -*-
# @Time : 2021/9/29 22:24
# @Author : 周孝尚
# @File : class.py
# @Software : PyCharm
class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def out(self):
        print(self.age + self.name)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


x = Student('18', 'Zhou')
x.out()

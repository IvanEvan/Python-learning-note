#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-4 下午3:26
# @Author  : Evan
# @Site    : 
# @File    : class_usage.py
# @Software: PyCharm Community Edition
class ClassName():
    def __init__(self):
        self.x = 1
    def m1(self):
        self.y = 2
        self.z = 5
        print('y=',self.y, 'z= ',self.z)
    def m2(self):
        self.y = 3
        self.z = self.x + 1
        print('y=',self.y, 'z=',self.z)
        self.m1()
myObj = ClassName()
myObj.m2()
print myObj.x
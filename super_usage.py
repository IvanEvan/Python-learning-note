#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-21 下午2:19
# @Author  : Evan
# @Site    : 
# @File    : super_usage.py
# @Software: PyCharm Community Edition
class A(object):                                     #python2 基类要继承object,   python3 不用
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super(B, self).add(m)                       #python2 super(class, self),   python3 super()
        self.n += 3

b = B()
b.add(2)
print(b.n)
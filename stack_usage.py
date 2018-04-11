#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-24 下午12:45
# @Author  : Evan
# @Site    : 
# @File    : stack_usage.py
# @Software: PyCharm Community Edition
import numpy as np

a = [np.random.randn(1, 2) for _ in range(4)]
b = np.stack(a, axis=0)
c = np.stack(a, axis=1)

e = np.array([[1,2],[3,4],[5,6]])
d = np.array([[11,12],[13,14],[15,16]])
f = np.stack((e,d), axis=1)
print f

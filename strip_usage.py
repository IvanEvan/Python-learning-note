#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-26 下午4:14
# @Author  : Evan
# @Site    : 
# @File    : strip_usage.py
# @Software: PyCharm Community Edition

'''s.strip(chars)使用规则：
        遍历chars里的每个字符，看是否在s的首尾，在就去掉
'''
str = 'hello world'
print str.strip()                # hello world
print str.strip('hello')         #  world
print str.strip('hello').strip() # world
print str.strip('heldo')         #  wor
print str.strip('heldo').strip() # wor

stt = 'h1h1h2h3h4h'
print stt.strip('h1')           # 2h3h4

s = '123459947855aaaadgat134f8sfewewrf7787789879879'
print s.strip('0123456789')    # aaaadgat134f8sfewewrf


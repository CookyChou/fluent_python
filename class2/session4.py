#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 17:56
# @Author  : bgzhou
# 生成器表达式

symbols = 'abcds'
print(tuple(ord(symbol) for symbol in symbols))

colors = ['Black', 'White']
sizes = ['S', 'M', 'L']

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
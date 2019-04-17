#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 18:08
# @Author  : bgzhou
# 元组可以作为一个记录来处理，在不进行重新排序的情况下，可以保持顺序

traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s %s' % passport)

# 进行拆包
for country, _ in sorted(traveler_ids):
    print(country)

a = ('a', 'b')
c, d = a
print(c)
print(d)

# 优雅的交换两个引用的值
c, d = d, c
print(c)
print(d)

def fun(a, b):
    print(a+b)

fun(*a)
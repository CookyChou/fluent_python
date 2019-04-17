#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 17:16
# @Author  : bgzhou
# 列表推导同filter和map的比较

symbols = 'abcde'
ascii1 = [ord(c) for c in symbols if ord(c) > 99]
print(ascii1)
ascii1 = list(filter(lambda a: a > 99, map(ord, symbols)))
print(ascii1)
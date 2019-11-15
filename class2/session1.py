#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 18:10
# @Author  : bgzhou

# symbols = 'abcde'
#
# codes = [ord(symbol) for symbol in symbols]
#
# print(codes)

symbols = "$¢£¥€¤"
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)
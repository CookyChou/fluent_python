#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 16:54
# @Author  : bgzhou

# {:16} 左边16个空格右对齐 {:^9} 居中两边相隔9个空格
print('{:^16} | {:^9} | {:^9}'.format('1', 'lat.', 'long'))

print('|{:^9}|{:<9}|{:>9}|'.format('1', '2', '3'))

# 大括号转义{}
print('{:.2f}{{保留两位小数}}'.format(3.1415926))
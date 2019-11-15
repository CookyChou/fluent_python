#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 17:50
# @Author  : bgzhou

import array

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

print([(color, size) for color in colors for size in sizes])

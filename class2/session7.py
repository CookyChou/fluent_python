#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 17:20
# @Author  : bgzhou

# 嵌套解包

metro_areas = [('Tokyo', 'JP', 36.933, (35.689722,139.691667)),
               ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
               ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
               ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
               ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)), ]

# 列表元组中的元组被当成是一个元素，无法进行拆分的
# for location, state, east, test1, test2 in metro_areas:
#     print(location, state, east, test1, test2)

# 使用(test1, test2) 这种方式就可以嵌套进行解包，非常方便
for location, state, east, (test1, test2) in metro_areas:
    print(location, state, east, test1, test2)
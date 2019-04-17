#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 9:53
# @Author  : bgzhou


def returnMax(list1):
    maxNum = max(list1)

    for j in range(len(str(maxNum))):
        k = []
        for i in list1:
            value = str(i)
            if j > len(value):
                break
            if value[j] > k[0]:
                k[0] = value[j]
                k[1] = value

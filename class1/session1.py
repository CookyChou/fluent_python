#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 16:39
# @Author  : bgzhou

from random import choice
import collections

Card = collections.namedtuple("Card", ['rank', 'suit'])


# 在python3中不需要显示的声明类继承于object
# 不能实现洗牌功能，因为这个里面的顺序是固定的

class DeskCard:
    # list("JQKA")直接将str转成list，list转成str为"".join(list)
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        # 列表生成式循环嵌套，只要将子层循环放在上层循环后面就可以
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    # 实现getitem方法可以实现切片的操作，[]操作和迭代操作
    def __getitem__(self, position):
        return self._cards[position]

    def spades_high(self, card):
        # 返回符合值的第一个list的index
        rank_value = self.ranks.index(card.rank)
        print(rank_value)
        print("*"*20)
        return rank_value * 10 + self.suit_values[card.suit]


if __name__ == '__main__':
    # 随机从序列中抽取元素
    # print(choice(DeskCard()))
    # print(len(DeskCard()))
    desk = DeskCard()
    # print(desk[12::13])
    # for i in desk:
    #     print(i)
    # # 反向迭代
    # for i in reversed(desk):
    #     print(i)

    # 一个集合类型如果没有实现__contains__方法，那么in运算符就会按顺序坐一次迭代搜索，in可以进行使用
    # 因为DeskCard是可以迭代的

    print(Card('Q', 'spades') in desk)
    print(Card('I', 'spades') in desk)
    for card in sorted(desk, key=desk.spades_high):
        print(card)
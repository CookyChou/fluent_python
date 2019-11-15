# import os
# t = (20, 9)
# l, n = t
# print(*t)
# print(os.path.split("/sfasdf/asdfasdfas"))
import random
import collections
from collections import namedtuple

Card = collections.namedtuple('Card', ['rank', 'suit'])
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.99, (35, 36))
print(City._fields)
print(tokyo.population)
print([x for x in range(9)])

t = '1234567'
print(t[::-1])
t = [x for x in range(9)]
for i in range(9):
    random.shuffle(t)
    print(t)

from collections import abc
my_dict = {}
print(isinstance(my_dict, abc.Mapping))
print(hash((1, 2, (3, 4))))
# print(hash((1, 2, [3, 4])))
fr = frozenset(range(9))
# print(isinstance(iterable, fr))
for i in fr:
    print(i)

from collections import OrderedDict

od = OrderedDict()
# 1位于列尾, 2位于列头
od[2] = "2"
od[1] = "1"
print(od)
# 弹出列头
# od.popitem(last=False)
# 弹出列尾
od.popitem()
print(od)

from collections import Counter
d = Counter()
d.update("abcdeefggg")
print(d.most_common(2))


# dict = {
#     2: "2",
#     1: "1"
# }
# dict.pop(2)
# print(dict)

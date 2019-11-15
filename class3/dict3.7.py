from types import MappingProxyType
# MappingProxyType提供一个视图索引，动态变化，可以通过索引访问查看，但是无法进行修改
d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy[1])
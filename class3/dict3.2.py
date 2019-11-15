# DIAL_CODES = [
#     (86, 'China'),
#     (91, 'India'),
#     (1, 'United States'),
#     (62, 'Indonesia'),
#     (55, 'Brazil'),
#     (92, 'Pakistan')
# ]
# country_code = {country: code for code, country in DIAL_CODES}
# print(country_code)

# import sys
# import re
# WORD_RE = re.compile(r'\w+')
# index = {}

# dict = {
#     'runoob': '菜鸟教程',
#     'google': 'Google 搜素'
# }
# list = ['runoob', 'google', 'tomcat']
# for i in list:
#     print(dict.setdefault(i, None))
# print(dict)
from collections import defaultdict


class StrKeyDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, item):
        return item in self.keys() or str(item) in self.keys()
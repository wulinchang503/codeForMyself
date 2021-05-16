import re

s = 'hello world!'
o = re.match('Hello', s, re.I)  # re.I 表示不区分大小写。
print(o)
print(o.group())
print(o.span())

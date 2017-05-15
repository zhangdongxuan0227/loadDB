#!/usr/bin/python
# -*- coding: utf-8 -*-
d = {'a': 1, 'b': 2, 'c': 3}
for i in d:
	print(i)

for s in d.values():
	print(s)

for u, v in d.items():
	print(u, v)

L = ['Hello', 'World', 'IBM', 'Apple']

e = [p.lower() for p in L]
print(e)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower()for s in L1 if isinstance(s,str)]
	#

print(L2)
#! /usr/bin/python
# -*- coding : latin-1 -*-

import os, sys
import math
"""
def quadratic(a, b, c):
	if b * b - 4 * a * c < 0:
		print("None")
	else:
		x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
		x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
		return x1, x2


s1 = quadratic(2, 3, 1)
s2 = quadratic(1, 3, -4)
print(s1,s2)
"""
def power(x, n):
	s3 = 1
	while n > 0:
		n = n - 1
		s3 = s3 * x
		print("------------")
		print("n:",n)
		print("x:",x)
	return s3
print(power(3,3))
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
print(enroll('zxc','man',7))
"""
def add_end(L=[]):
    L.append('END')
    return L
add_end()
add_end()
print(add_end())
"""
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
add_end()
#add_end()
print(add_end())
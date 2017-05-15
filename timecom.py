#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'Administrator'

from time import time


def plus_test():
	t = time()
	s = ''
	for i in range(1000000):
		s += 'test'
		print(time())
		print(t)
	print(time() - t)


def join_test():
	t = time()
	li = []
	for i in range(1000000):
		li.append('test')
	s = ''.join(li)
	print(time() - t)


plus_test()
join_test()

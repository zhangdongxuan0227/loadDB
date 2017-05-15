#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
def fact(n):
	if n==1:
		return 1
	else:
		return n * fact(n-1)

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
	    return product
    return fact_iter(num - 1, num * product)
"""

def mov(n, a, b, c):
    if(n == 1):
        print('%c-->%c',(a, c))
        #只有一个盘子，可以直接从a移动到c
    else:
        #通过分步减而治之
        mov(n-1, a, c, b)
        #先把上面的n-1个盘子借助c从a移到b
        mov(1, a, b, c)
        #再把a最下面的一个盘子移到c
        mov(n-1, b, a, c)
        #再把b上的n-1个盘子借助a移动到c
ss = mov(3, 'A', 'B', 'C')
print(ss)

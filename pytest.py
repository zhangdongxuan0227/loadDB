#!/usr/bin/python
# -*- coding: utf-8 -*-
# _author__ = 'Administrator'
#
# import xlrd
#
# f = open('D:\pytest.txt')  #首先先创建一个文件对象
# # sr = f.read(4)
# fr = f.readline(4)  #用read()方法读取文件内容
# fr1 = f.readline(4)
# print (fr,fr1)#打印所读取到的内容
#
# # print (sr)
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n
#
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
#
# bar()

# def foo(s):
#     n = int(s)
#     print('>>> n = %d' % n)
#     return 10 / n
#
# def main():
#     foo('0')
#
# main()

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
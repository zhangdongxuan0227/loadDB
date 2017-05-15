#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'zhangdongxuan'
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if 3 < len(name):
        return _private_1(name)
    else:
        return _private_2(name)
st = input('shuru name:')
print('your name is',(st))
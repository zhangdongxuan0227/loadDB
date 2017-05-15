#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'Administrator'
import urllib.parse
import urllib.request
f = urllib.request.urlopen('http://www.baidu.com')
firstline = f.readline()

print(firstline)
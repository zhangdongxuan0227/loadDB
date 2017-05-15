#!/usr/bin/python
# -*- coding: utf-8 -*-

#import test5


'''
n = 1
while n <11:
    if n >= 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
'''
d={'zxc':12,'ccc':13,'xxx':22}
c=[1,2,3,'zxc','dkjnihao']
s1=set([1,2,3,3])
s2=set([3,5.6])
e='abc'
e.replace('a','A')
#s.add(4)
#s.remove(3)
d.pop('ccc')
c.append('ddd')
c.insert(2,'zhjj11212')
print (len(c))
print(c[-1])
print(d)
print(c)
print(s1|s2)
print(e)
n1 = 255
n2 = 1000

f=int

print(f('8989'))
print('n1:',hex(n1))
print('n2:',hex(n2))
print(max(1,2,10))
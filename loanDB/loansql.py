#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'Administrator'

import pymysql
#创建连接，数据库ip，端口号，账号，密码，数据库名，字符集
conn = pymysql.connect(host = '10.10.23.79',port = 3306,user = 'xzdh',password = '5Fy7ttDgRY',db = 'sales',charset='UTF8')
#创建游标
cursor = conn.cursor()

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

#执行sql
effect_row = cursor.execute('SELECT * FROM t_loan_type_dictionary;')



res = cursor.fetchall()

print(res)
#提交
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()
#hsjhdsjfhsdjf
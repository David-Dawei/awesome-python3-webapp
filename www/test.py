# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 00:33:59 2018

@author: wdw
"""

import orm
from models import User, Blog, Comment
import asyncio

print('L12')
loop = asyncio.get_event_loop()
print('L14')
def test():
    yield from orm.create_pool(loop,user='www-data',password='www-data',db='awesome')
    u = User(name='Test4',email='Test4@example.com',passwd='1234567890',image='about:blank')
    yield from u.save()
#    yield from orm.destory_pool()
print('L20')
loop.run_until_complete(test())
#loop.stop()
#loop.run_forever()
loop.close()

print("hhhhhhh")
print("hhhhhhh")
print("hhhhhhh")

'sql check code'
data = User.findAll()
for d in data:
    print(d)
#
#
#import mysql.connector
#conn = mysql.connector.connect(user='www-data',password='www-data',db='awesome')
#cursor=conn.cursor()
#cursor.execute('select * from users')
#data = cursor.fetchall()
#print(data)
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 19:56:42 2018

@author: wdw
"""

from coroweb import get, post
from models import User, Blog, Comment

@get('/')
def index(request):
    users = yield from User.findAll()
    return {
            '__template__':'test.html',
            'users' : users
            }
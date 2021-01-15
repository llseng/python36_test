# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-13 15:36:28
# @LastEditors: llseng
# @LastEditTime: 2021-01-13 15:40:42
#

import threading as tding, time

n_rlock = tding.RLock()
# n_rlock = tding.Lock()

def f():
    with n_rlock:
        g()
        h()

def g():
    with n_rlock:
        h()
        print( "print n" )

def h():
    with n_rlock:
        print( "print m" )


f()
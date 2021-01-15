# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-15 11:20:18
# @LastEditors: llseng
# @LastEditTime: 2021-01-15 11:20:18
#

import threading, time
from random import randint

def print_action():
    print( threading.get_ident(), 'ACTION' )

print_exit = 0
print_barrier = threading.Barrier( 3, print_action, 5 )

def print_func( name ):
    print( "T", name, threading.get_ident(), 'START' )

    stime = time.time()
    try:
        print_barrier.wait()
    except Exception:
        print( "T", name, threading.get_ident(), 'wait timeout' )
    finally:
        etime = time.time()
        print( "T", name, threading.get_ident(), 'wait', round( etime - stime, 4 ) )

    while True:
        if print_exit: break
        print( "T", name, threading.get_ident(), 'print' )
        time.sleep( 0.5 )

    print( "T", name, threading.get_ident(), 'END' )

for x in [1,2]:
    threading.Thread( target=print_func, args=(x,) ).start()

print( "Main sleep 2", threading.get_ident() )
time.sleep( 2 )

for x in [3,4]:
    threading.Thread( target=print_func, args=(x,) ).start()

for x in range( 5 ):
    print( "n_waiting", print_barrier.n_waiting )
    print( "parties", print_barrier.parties )
    print( "broken", print_barrier.broken )
    print( "Main sleep 1", threading.get_ident() )
    time.sleep( 1 )

print_exit = 1
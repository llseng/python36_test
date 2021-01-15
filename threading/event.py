# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-15 10:48:58
# @LastEditors: llseng
# @LastEditTime: 2021-01-15 10:48:58
#

import threading, time
from random import randint

print_event = threading.Event()
print_exit = 0

def print_func( name ):
    print( "T %s" % name, "START" )

    while True:
        if print_exit: break
        s_time = time.time()
        print_event.wait()
        e_time = time.time()
        print( "T %s" % name, "print", round( e_time - s_time, 4 ) )
        time.sleep( 0.5 )

    print( "T %s" % name, "END" )

if __name__ == "__main__":
    for x in range( 5 ):
        threading.Thread( target = print_func, args=( "thread_%d" % x,) ).start()
    
    print_event.set()

    i = 10
    while i > 0:
        sleep_time = randint( 1, 10 )
        print( "Main", "sleep %d" % sleep_time )
        time.sleep( sleep_time )

        clear_time = randint( 1, 10 )
        print( "Main", "clear %d" % clear_time )
        print_event.clear()
        time.sleep( clear_time )
        print_event.set()
        print( "Main", "clear end" )

        i -= 1

print_exit = 1
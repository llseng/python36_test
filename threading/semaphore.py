# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-14 15:39:14
# @LastEditors: llseng
# @LastEditTime: 2021-01-14 15:39:14
#

import threading, time
from random import randint

task_exit = 0
task_list = [1, 2, 4]
# sem = threading.Semaphore( len( task_list ) )
sem = threading.BoundedSemaphore( len( task_list ) )

def test( ):
    task_list.append( randint( 1, 100 ) )
    sem.release()

def task_consumer( name ):
    print( "T %s" % name, "START" )

    while True:
        if task_exit: break

        stime = time.time()
        status = sem.acquire( True, 4 )
        etime = time.time()
        print( "T %s" % name, "acquire", etime - stime )
        if not status:
            print( "T %s" % name, "acquire timeout")
            continue

        print( "T %s" % name, "task", task_list.pop() )

    print( "T %s" % name, "END" )

for x in range( 4 ):
    threading.Thread( target=task_consumer, args=("thread_%d" % x,) ).start()

i = 20
try:
    while i > 0:
        sleep_time = randint( 1, 5 )
        print( "main sleep", sleep_time )
        time.sleep( sleep_time )
        print( "main sleep end" )

        rnum = randint( 1, 10 )
        print( "main rnum", rnum )
        for x in range( rnum ):
            print( "main append task" )
            test()
        
        i -= 1
except Exception as e:
    print( "main error", e )

    
task_exit = 1
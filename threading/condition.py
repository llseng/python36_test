# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-13 16:01:13
# @LastEditors: llseng
# @LastEditTime: 2021-01-13 16:01:13
#

import threading as tding, time
from random import randint

cond_lock = tding.Lock()
cond = tding.Condition( cond_lock )

worker_exit = 0
task_list = []

def worker( name ):
    print( "Worker %s" % name, "Start" )
    
    while True:
        with cond:
            if worker_exit: break
            if not len( task_list ):
                print( "Worker %s" % name, "wait..." )
                cond.wait()
                print( "Worker %s" % name, "wake!" )
            if worker_exit: break
            if len( task_list ):
                task = task_list.pop()
            else:
                continue

        print( "Worker %s" % name, "task start" )

        sleep_time = task.get( 'sleep_time', 1 )
        time.sleep( sleep_time )
        print( "Worker %s" % name, "task", task )

        print( "Worker %s" % name, "task end" )
        

    print( "Worker %s" % name, "End" )

def task_push( **args ):
    with cond:
        task_list.append( args )
        cond.notify()

def on_worker_exit( ):
    global worker_exit
    with cond:
        worker_exit = 1
        cond.notify_all()

for x in range( 4 ):
    tding.Thread( target=worker, args=('%d' % x,) ).start()

task_id = 0
while task_id < 20:
    print( 'main', task_list )

    stime = randint( 1, 10 )
    print( 'main', 'sleep %d' % stime )
    time.sleep( stime )

    print( 'main', task_list )
    
    for x in range( randint( 1, 5 ) ):
        task_push( sleep_time = randint( 1, 10 ), task_id = task_id )
        task_id += 1
    
print( 'main', 'on_worker_exit' )
on_worker_exit()
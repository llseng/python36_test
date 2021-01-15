# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-15 16:27:15
# @LastEditors: llseng
# @LastEditTime: 2021-01-15 16:27:16
#

import multiprocessing as mp, time, os

def print_func( name ):
    stime = time.time()
    i = 5
    ppid = os.getppid()
    pid = os.getpid()
    print( "P", name, ppid, pid, __name__ )
    print( "P", name, pid, "START" )

    while i > 0:
        print( "P", name, pid, "sleep 1" )
        time.sleep( 1 )
        i -= 1
    
    etime = time.time()
    print( "P", name, pid, "END", round( etime - stime, 4 ) )

if __name__ == "__main__":
    stime = time.time()
    pros = []
    for x in range( 5 ):
        pros.append( mp.Process( target=print_func, args=( "p_%d" % x,) ) )
    
    for x in pros:
        x.start()

    etime = time.time()
    print( "Time", round( etime - stime, 4 ) )

    for x in pros:
        x.join()

    etime = time.time()
    print( "Time", round( etime - stime, 4 ) )

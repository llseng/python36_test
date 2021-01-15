# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-13 10:39:08
# @LastEditors: llseng
# @LastEditTime: 2021-01-13 11:52:23
#

import threading, time

class LockTest( threading.Thread ):
    """
    docstring
    """
    def __init__( self, name ):
        super().__init__()
        self.setName( name )
    
    def run( self ):
        print( "LT %s Start" % self.getName() )
        while True:
            node = get_print_node( )
            if node == None:
                break
            print( "LT %s:" % self.getName(), node )
        print( "LT %s End" % self.getName() )

i = 0
list_lock = threading.Lock()
use_lock = True

def get_print_node():
    global i
    if use_lock:
        with list_lock:
            if i > 100:
                return None
            node = i
            time.sleep(0.1)
    else:
        if i > 100:
            return None
        node = i
        time.sleep(0.1)
    i += 1
    return node

lock_threads = []
for x in range( 5 ):
    lock_threads.append( LockTest( "lock_test_%d" % x ) )

for x in lock_threads:
    x.start()

for x in lock_threads:
    x.join()





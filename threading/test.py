# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-12 17:09:40
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-12 18:21:50

import random, time, threading

class TestThread( threading.Thread ):
    """测试线程"""
    def __init__(self, name):
        super().__init__( daemon=True )
        self.setName( name )

    def run(self):
        print( "TT %s Start" % self.getName() )
        for x in range( random.randint(5, 10) ):
            time.sleep( 1 )
            print( "TT %s:" % self.getName(), x )
        print( "TT %s End" % self.getName() )

tts = []
for x in range( 5 ):
    tts.append( TestThread( "test_thread_%d" % x ) )

for x in tts:
    print( "start", x )
    x.start()
    print( "start end", x )

for x in tts:
    print( "join", x )
    x.join()
    print( "join end", x )

print( "Exit" )
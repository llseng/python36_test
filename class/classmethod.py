# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-20 11:25:12
# @LastEditors: llseng
# @LastEditTime: 2021-01-20 11:25:13
#

from time import time, localtime, sleep

class Clock():
    """
    时钟
    """
    @classmethod
    def now( cls ):
        ctime = localtime( time() )
        return cls( ctime.tm_hour, ctime.tm_min, ctime.tm_sec )

    def __init__( self, h, m, s ):
        self._h = h
        self._m = m
        self._s = s

    def run( self ):
        self._s += 1
        if self._s == 60:
            self._s = 0
            self._m += 1
            if self._m == 60:
                self._m = 0
                self._h += 1
                if self._h == 24:
                    self._h = 0
    
    def show( self ):
        return "%02d:%02d:%02d" % ( self._h, self._m, self._s )

if __name__ == "__main__":
    # ck = Clock.now()
    ck = Clock( 23, 59, 55 )
    
    i = 100
    while i > 0:
        print( ck.show() )
        ck.run()
        sleep( 1 )
        i -= 1
    
    print( 'exit' )
    
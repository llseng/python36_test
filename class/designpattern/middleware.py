# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-04-14 11:45:18
# @LastEditors: llseng
# @LastEditTime: 2021-04-14 11:45:18
#

class Middleware( ):

    def __init__( self ):
        self.handlers = []

    @staticmethod
    def isCallable( f ):
        return True
    
    def pushHandler( self, handler ):
        if not callable( handler ):
            return False
        if handler.__code__.co_argcount != 2:
            return False
        self.handlers.append( handler )
        return True

    def packHandler( self ):
        def next( p ):
            return p
        for h in self.handlers[-1::-1]:
            def f( handler=h, next=next ):
                def fn( p ):
                    return handler(p, next)
                fn.__name__ = getattr(handler, '__name__')
                return fn
            next = f()
        return next

if __name__ == '__main__':
    def Test( p, n ):
        return True

    m = Middleware()
    
    @m.pushHandler
    def Am( p, n ):
        print('Am Start')
        p = p + '_Am'
        print('Am End')
        return n( p )

    @m.pushHandler
    def Bm( p, n ):
        print('Bm Start')
        r = n( p )
        r = r + '_Bm'
        print('Bm End')
        return r

    @m.pushHandler
    def Cm( p, n ):
        print('Cm Start')
        p = p + '_Cm'
        print('Cm End')
        return n( p )
        
    app = m.packHandler()
    print( app )
    print( app('data') )

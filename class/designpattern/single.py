# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-04-15 16:14:06
# @LastEditors: llseng
# @LastEditTime: 2021-04-15 16:14:07
#

import threading

class SingleMeta( type ):
    """
    单例模式元类
    """
    def __init__( cls, *args, **kwargs ):
        cls.__instance = None
        cls.__rlock = threading.RLock()
        super().__init__( *args, **kwargs )
    
    def __call__( cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__rlock:
                if cls.__instance is None:
                    cls.__instance = super().__call__( *args, **kwargs )
        return cls.__instance

class A( metaclass=SingleMeta ):
    pass

class B( metaclass=SingleMeta ):
    pass

class C( metaclass=SingleMeta ):
    pass

class Foo:
    pass

class Zoo:
    pass

if __name__ == "__main__":
    a = A()
    b = A()
    c = C()
    d = Foo()
    e = Foo()
    f = Zoo()

    print( a, b, c, d, e, f )
    print( id(a), id(b), id(c), id(d), id(e), id(f) )
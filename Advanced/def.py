# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-25 16:18:23
# @LastEditors: llseng
# @LastEditTime: 2021-01-25 16:18:24
#

import time, functools, threading

# 高阶函数 (参数是函数的函数)

tmp1 = list( map( lambda x: x ** 2, filter( lambda x: x % 4, range(10) ) ) )
print( tmp1 )

tmp2 = [ x ** 2 for x in range(10) if x % 4 ]
print( tmp2 )

# 装饰器函数

def record_time( func ):

    @functools.wraps(func)
    def wrapper( *args, **kwargs ):
        start = time.time()
        result = func( *args, **kwargs )
        print( f"{func.__name__} run time: {time.time() - start}" )
        return result
    
    return wrapper

@record_time
def run_time_test():
    time.sleep(0.2)

run_time_test()

def record( output=print ):
    ''' 参数化装饰器 '''
    def decorate( func ):
        
        @functools.wraps( func )
        def wrapper( *args, **kwargs ):
            start = time.time()
            result = func( *args, **kwargs )
            output( func.__name__, time.time() - start )
            return result
        
        return wrapper
    
    return decorate

@record(output=print)
def run_time_test2():
    time.sleep( 0.3 )

run_time_test2( )

# 实现单例装饰器
instance = {}

def singleton( cls ):
    ''' 单例装饰器 '''
    instance = {}
    lock = threading.RLock()
    
    @functools.wraps( cls )
    def wrapper( *args, **kwraps ):
        if not cls in instance:
            with lock:
                if not cls in instance:
                    instance[ cls ] = cls( *args, **kwraps )
            
        print( instance )
        return instance[ cls ]

    return wrapper

@singleton
class Att():
    pass

@singleton
class Btt():
    pass

@singleton
class Ctt():
    pass

a = Att()
b = Att()
c = Att()
d = Btt()
e = Btt()
f = Ctt()

print( id(a), id(b), id(c), id(d), id(e), id(f) )

# 类对象可以放在 set集合 里
tmp_set = {a, b, c, d, e, f}
print( tmp_set )

# 元编程 元类

class singletonMeta( type ):
    def __init__( cls, *args, **kwraps ):
        cls.__instance = None
        cls.__rlock = threading.RLock()
        super().__init__( *args, **kwraps )
    
    def __call__( cls, *args, **kwraps ):
        if cls.__instance is None:
            with cls.__rlock:
                if cls.__instance is None:
                    cls.__instance = super().__call__( *args, **kwraps )
            
        return cls.__instance

print( singletonMeta )

class Aoo( metaclass=singletonMeta ):
    pass
class Boo( metaclass=singletonMeta ):
    pass
class Coo( metaclass=singletonMeta ):
    pass

ol = []
ol.append( Aoo() )
ol.append( Aoo() )
ol.append( Aoo() )
ol.append( Boo() )
ol.append( Boo() )
ol.append( Coo() )

print( ol )
print( set( ol ) )
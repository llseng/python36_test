# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-26 15:24:21
# @LastEditors: llseng
# @LastEditTime: 2021-01-26 15:24:22
#

import redis

r = redis.StrictRedis('localhost', 6379, 0 )

print( r.keys() )

print( 'set', r.set( 'foo', 'test' ) )
print( 'get', r.get( 'foo' ) )
print( 'keys', r.keys( ) )
print( 'delete', r.delete( 'foo' ) )
print( 'keys', r.keys() )

r.close()
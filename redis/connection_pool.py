# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-26 15:34:59
# @LastEditors: llseng
# @LastEditTime: 2021-01-26 15:35:00
#

import redis, time

pool = redis.ConnectionPool( host='localhost', port=6379, decode_responses=True )
r = redis.Redis( connection_pool=pool )
r.set( 'name', 'Python', px=1 )
time.sleep( 0.5 )
print( r.get( 'name' ) )

print( r.set( 'name', 'Python', nx=True ) )
print( r.get( 'name' ) )

print( r.keys() )
r.close()
# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-09 14:55:00
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-09 15:07:53

tuple1 = ('Google', 'Runoob', 1997, 2000)
tuple2 = (1, 2, 3, 4, 5 )
tuple3 = (["a", "b"], "c", "d")
tuple4 = ('red', 'green', 'blue', 'yellow', 'white', 'black')

print( 'type( tuple1 )', type( tuple1 ) )

print( 'id( tuple3 )', id( tuple3 ) )
print( 'tuple3', tuple3 )
tuple3[0][0] = 'A'
print( 'id( tuple3 )', id( tuple3 ) )
print( 'tuple3', tuple3 )

print( 'type( {} )', type( {} ) )
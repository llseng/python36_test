# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-09 15:47:35
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-09 17:34:46

import sys

print( sys.path )

a, b = 0, 1
while b < 100:
    print( b, end = ',' )
    a, b = b, a + b

print()
for x in range( 0, 5 ):
    print( x, end = ',' )

print( None )
if None: print( 'hello' );

# 迭代器
l = [9, 12, 5, 5543, 66]
it = iter( l )

while True:
    try:
        print( next( it ), end = ',' );
    except Exception as e:
        print( type( e ) )
        break

class iterClass:
    def __iter__( self ):
        self.a = 0
        return self

    def __next__( self ):
        x = self.a
        if x > 20: raise StopIteration
        self.a += 1
        return x

itcObj = iterClass()
itc = iter( itcObj )

while True:
    try:
        print( next( itc ), end = ' ' );
    except Exception as e:
        print( type( e ) )
        break

'''
生成器
'''

def fiter( n ):
    a, b, c = 0, 1, 0
    while True:
        if c > n: return

        yield a
        a, b = b, a + b
        c += 1

f = fiter( 20 )

print( f )

while True:
    try:
        print( next( f ), end = ' ' );
    except Exception as e:
        print( type( e ) )
        break

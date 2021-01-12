# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-09 15:28:34
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-09 15:44:19

set1 = set( ['a', 'b', 'c', 'd'] )
set2 = set( ('A', 'B', 'C', 'D') )
set3 = {1, 2, 3, 4}
set4 = set()

strset1 = set("hello python")
strset2 = set("hello set")

print( 'set1', set1 )
print( 'set2', set2 )
print( 'set3', set3 )
print( 'set4', set4 )
print( 'strset1', strset1 )
print( 'strset2', strset2 )

print( 'type( set1 )', type( set1 ) )
print( 'type( set2 )', type( set2 ) )
print( 'type( set3 )', type( set3 ) )
print( 'type( set4 )', type( set4 ) )
print( 'type( strset1 )', type( strset1 ) )
print( 'type( strset2 )', type( strset2 ) )

print( 'set1 | set2', set1 | set2 )
print( 'set1 & set2', set1 & set2 )

print( 'strset1 | strset2', strset1 | strset2 )
print( 'strset1 & strset2', strset1 & strset2 )

set1.add( 'e' )
set2.add( 'E' )
print( 'set1', set1 )
print( 'set2', set2 )
set1.remove( 'a' )
set2.remove( 'A' )
print( 'set1', set1 )
print( 'set2', set2 )
set1.discard('c')
set2.discard('C')
print( 'set1', set1 )
print( 'set2', set2 )
print( 'set1.pop()', set1.pop() )
print( 'set2.pop()', set2.pop() )
print( 'set1', set1 )
print( 'set2', set2 )


print( 'len( set3 )', len( set3 ) )
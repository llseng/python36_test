# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-09 14:28:10
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-09 14:53:16
# 
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']

print( 'list1', list1 )
print( 'list2', list2 )
print( 'list3', list3 )
print( 'list4', list4 )

print( 'list1[-2:]', list1[-2:] )
print( 'list2[1:-1]', list2[1:-1] )
del list3[-1]
print( 'del list3[2:-2]', list3 )
print( 'len( list4 )', len( list4 ) )
print( 'list1[-2:] + list2', list1[-2:] + list2 )
print( '2000 in (list1[-2:] + list2)', 2000 in (list1[-2:] + list2) )
print( 'list2 * 4', list2 * 4 ) 

for x in list4:
    print( x )

print( '[ list1, list2 ]', [ list1, list2 ] )
print( 'min( list2 )', min( list2 ), 'max( list2 )', max( list2 ) )

tmp_list = list2
cpy_list = list2.copy()
print( 'tmp_list', tmp_list )
print( 'cpy_list', cpy_list )
list2.remove( 5 )
print( 'list2', list2 )
print( 'tmp_list', tmp_list )
print( 'cpy_list', cpy_list )
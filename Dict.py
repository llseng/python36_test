# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-09 15:08:11
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-09 15:28:21

dict1 = {'name': 'ali', 'age': 24, 1: 'name'}
dict2 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print( 'dict1', dict1 )
print( 'dict2', dict2 )
print( 'dict2[\'Name\']', dict2['Name'] )

dict1['age'] = dict1['age'] + 1
print( 'dict1', dict1 )

print( '\'name\' in dict1', 'name' in dict1 )
del dict1[1]
print( 'dict1', dict1 )

print( 'dict1.keys()', dict1.keys() )
print( 'dict1.items()', dict1.items() )

for i, j in dict1.items():
    print('i, j', i, j)

for x in dict1.keys():
    print( 'x', x, 'dict1[x]', dict1[x] )

dict1.clear()
print( 'dict1', dict1 )

print( 'type( {\'a\'} )', type( {'a'} ) )
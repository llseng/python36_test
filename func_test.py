# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-09 16:44:25
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-09 17:24:26

# 普通函数
def sum( a, b ):
    return a + b

def max( a, b ):
    if a > b:
        return a
    return b

def min( a, b ):
    if a < b:
        return a
    return b

print( "sum( 10, 9 )", sum( 10, 9 ) )
print( "sum( b = 10, a = 9 )", sum( b = 10, a = 9 ) )

'''
传不可变参
'''
a, b = 22, 12
print( 'a, b', a, b )
print( 'id( a ), id( b )', id( a ), id( b ) )
a = sum( a, b )
b = max( a, b )
print( 'a, b', a, b )
print( 'id( a ), id( b )', id( a ), id( b ) )

'''
传可变参
'''
def set_list_0( l, a ):
    '''*set_list_0( l, a )
*l 列表
*a 值'''
    l[0] = a
    return l

l1 = [2, 2, 3, 4]
print( 'l1, id( l1 )', l1, id( l1 ) )
set_list_0( l1, 1 )
print( 'l1, id( l1 )', l1, id( l1 ) )
print( "set_list_0.__doc__" )
print( set_list_0.__doc__ )

def pinfo( name, age = 10 ):
    print( 'name', name, 'age', age )

'''
必须参数
'''
print( "pinfo( '名字', '年龄' )" )
pinfo( '名字', '年龄' )
'''
关键字参数
'''
print( "pinfo( age = '年龄', name = '名字' )" )
pinfo( age = '年龄', name = '名字' )
'''
默认参数
'''
print( "pinfo( name = '名字' )" )
pinfo( name = '名字' )

'''
不定长参数
'''
# 元组
def pinfo1( name, age = 12, *other ):
    print( 'name', name, 'age', age )
    print( other )
# 字典
def pinfo2( name, age = 12, **other ):
    print( 'name', name, 'age', age )
    print( other )

print( "pinfo1( 'ali', 10, 1, 2, 6 )" )
pinfo1( 'ali', 10, 1, 2, 6 )
print( "pinfo2( 'ali', 10, a = 1, b = 2, c = 6 )" )
pinfo2( 'ali', 10, a = 1, b = 2, c = 6 )

'''
匿名函数
'''
lsum = lambda a, b: a ** b
print("lsum( 10, 12 )", lsum( 10, 12 ))
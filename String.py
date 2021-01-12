# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-09 11:49:36
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-09 14:25:03

import sys

s1 = "hello python"
s2 = "hello python36"

print( "s1:", s1 )
print( "s1[:]:", s1[:] )
print( "s2:", s2 )
print( "s2[:]:", s2[:] )
print( "s1[0:]:", s1[0:] )
print( "s1[1:]:", s1[1:] )
print( "s2[0:-2]:", s2[0:-2] )
print( "s2[0:-2:2]:", s2[0:-2:2] )

s1 += " !"
s2 += " !"

print( "s1:", s1 )
print( "s2:", s2 )
print( "\a" )

print( "a in s1: %d" % ('a' in s1), "h in s1: %d" % ('h' in s1) )
print( "o in s2: %d" % ('o' in s2), "p in s2: %d" % ('p' in s2) )

print( "s1.swapcase():", s1.swapcase() )
print( "f-string" )
print( "'s1 \%s' \% s1:", 's1 %s' % s1 )
print( "f's1 {s1}':", f's1 {s1}' )

print( "s1:",s1,'len',len( s1 ) )

print( "len('测试'):", len('测试') )

print( "sys.version_info:", sys.version_info )
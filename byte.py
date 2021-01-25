# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-23 17:49:58
# @LastEditors: llseng
# @LastEditTime: 2021-01-23 17:49:59
#


b64 = "waswwaswwa"
bb64 = b"waswwaswwa"

def f( s ):
    if not isinstance( s, bytes ):
        s = bytes( s, encoding = "utf8" )
    m = len( s ) % 4
    if m:
        s += b'=' * (4 - m)
    return s

def s( s ):
    if not isinstance( s, bytes ):
        s = bytes( s, encoding = "utf8" )
    spos = s.find( b'=' )
    if spos:
        s = s[0: spos]
    return s

print( f( b64 ) )
print( f( bb64 ) )

print( s( f( b64 ) ) )
print( s( f( b64 ) ) )
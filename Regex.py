# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-11 16:21:20
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-11 16:47:32

import re

print( "match---------" )
print( re.match( 'www', 'www.baidu.com' ).span() )
print( re.match( 'baidu', 'www.baidu.com' ) )

print( "search---------" )
print( re.search( 'www', 'www.baidu.com' ).span() )
print( re.search( 'baidu', 'www.baidu.com' ).span() )

print( "sub---------" )
print( re.sub( r'\d*', '', 'ww9418w89461.54b5a165654id498u651.8c984o6m128' ) )
print( re.sub( r'[a-zA-Z\.]', '', 'ww9418w89461.54b5a165654id498u651.8c984o6m128' ) )
print( re.sub( r'(\d+)', '[\\1]', 'ww9418w89461.54b5a165654id498u651.8c984o6m128' ) )

print( 'compile---------' )
wp = re.compile( r'\w+' )
dp = re.compile( r'\d+' )

w = wp.match( "asdasdqw" )
print( w )

if w:
    print( w.group() ) 
    print( w.start() ) 
    print( w.end() ) 
    print( w.span() ) 

d = dp.match( "5165" )
print( d )

if d:
    print( d.group() ) 
    print( d.start() ) 
    print( d.end() ) 
    print( d.span() ) 

d = re.compile( r'(\d+) (\d+)' ).search( "5 1 65 654" )
print( d )

if d:
    print( d.group() ) 
    print( d.groups() ) 
    print( d.start() ) 
    print( d.end() ) 
    print( d.span() ) 

print( 'findall---------' )

print( re.findall( r'\d+', "64651 8516854 64646455 16 51 651 51565 41 545 64" ) )
print( re.findall( r'\w+', "safdjaqfj n9h9ah8d9asd98sdh9aqwdwqidqo 8516854 64646455 16 51 651 51565 41 545 64" ) )

print( 'finditer---------' )

it = re.finditer( r'\d+', "654a5s4d1wq981qwd1asda65sdq98516asd418qw1as65d9as194" )
for x in it:
    print( x )

print( "split---------" )

print( re.split( r"\D+", "64651 8516854 64646455 16 51 651 51565 41 545 64" ) )
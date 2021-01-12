# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-11 15:23:19
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-11 18:28:28

import os, glob, sys, re, random, time
from urllib.request import urlopen

print( 'os.path', os.path )
print( 'os.getcwd', os.getcwd() )
print( 'os.getcwdb', os.getcwdb() )
print( 'os.getenv', os.getenv('path') )
for key in os.environ.keys( ):
    print( "%s: %s" % ( key, os.environ[key] ) )

print( 'os.system( "dir" )', os.system( "dir" ) )
print( 'glob.glob("*.py")', glob.glob("*.py") )
print( 'sys.argv', sys.argv )

print( re.findall( r'\w+', "asd asdq1da asd654 asda5" ) )
print( "one too three".replace( 'too', 'two' ) )

print( random.random() )
print( random.randrange(100) )
print( random.choice( ['a', 'b', 'c', 'd', 'e', 'f'] ) )

for line in urlopen( "http://baidu.com" ):
    print( 'type( line )', type( line ) )
    print( line )

print( urlopen( "http://baidu.com" ).read().decode() )

print( time.time() )

print( 'test' + str( 1 ) )

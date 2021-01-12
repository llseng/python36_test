# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-09 17:58:33
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-11 11:22:57

# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。
import pickle
import pprint

a = "A\n"
print( repr( a ) )

for x in range(1,10):
    print( repr( x ).rjust(1), repr( x ** 2 ).rjust(2), repr( x ** 3 ).rjust(3) )

for x in range(1,10):
    print( "{0:2d} {1:3d} {2:4d}".format(x, x**2, x**3) )

# i = input( "输入" )
# print( 'i', i )

f1 = open( '../test.log', 'r+' )

print( "f1.read()", f1.read() )
print( "f1.tell()", f1.tell() )

f1.seek( 0 )

print( "f1.readline()", f1.readline() )
print( "f1.tell()", f1.tell() )
print( "f1.readline()", f1.readline() )
print( "f1.tell()", f1.tell() )
print( "f1.readline()", f1.readline() )
print( "f1.tell()", f1.tell() )
print( "f1.readline()", f1.readline() )
print( "f1.tell()", f1.tell() )
print( "f1.readline()", f1.readline() )
print( "f1.tell()", f1.tell() )
print( "f1.readline()", f1.readline() )
print( "f1.tell()", f1.tell() )

print( "f1.write( \"138680032\\n\" )", f1.write( "138680032\n" ) )
print( f1.closed )

f1.seek( 0 )
print( "f1.readlines()", f1.readlines() )
print( "f1.tell()", f1.tell() )

f1.close()
print( f1.closed )

print( "with test----------" )

with open( '../test.log', "r" ) as f2:
    print( f1.closed )
    print( f2.read() )
print( f1.closed )

print( "pickle test----------" )

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

print( 'data1', data1 )
print( 'selfref_list', selfref_list )

output = open( "data.pkl", "wb" )

pickle.dump( data1, output )
pickle.dump( selfref_list, output, -1 )

output.close()

dpkl = open( "data.pkl", "rb" )
ddata1 = pickle.load( dpkl )
ddata2 = pickle.load( dpkl )

dpkl.close()

print( 'ddata1', ddata1 )
print( 'ddata2', ddata2 )
pprint.pprint( ddata1 )
pprint.pprint( ddata2 )

dpkl.close()

f3 = open( "truncate_test.log", "w+" )
f3.writelines( ['192.168.0.140 - - [11/Jan/2021:10:20:21 +0800]\n', "POST /suvapi/Interface/data/ad_count.php HTTP/1.1\n", '200 51\n', "http://wxclient.gzqidong.cn/House/cibin_desk/index.html" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36\n", "-\n", '0.147\n', '0.147\n'] )

f3.seek( 0)

print( f3.readline() )
print( f3.tell() )
f3.truncate( )
print( f3.readlines() )
# f3.truncate( 10 )

f3.close()
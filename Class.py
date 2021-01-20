# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-11 11:53:03
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-11 14:56:22

class Foo():
    """docstring for Foo"""
    __small_name = ''
    def __init__(self):
        self.name = 'default'
        self.age = 0
        self.__small_name = 'small_def'

    def get( self ):
        return self.__small_name

    def __get( self ):
        return 'private_' + self.get()

    def get_private( self ):
        return self.__get()

class Goo( Foo ):
    """ Goo( Foo ) """
    def __init__( self, name ):
        super( Goo, self ).__init__( )
        self.name = name

    def get( self ):
        return super( Goo, self ).get( ) + '_' + self.name

foo = Foo()
print( foo.name )
print( foo.age )
try:
    print( foo.__small_name )
except Exception as e:
    print( e )
    print( foo.get() )

print( foo.get_private() )

goo = Goo( "lisa" )
print( goo.name )
print( goo.age )

try:
    print( goo.__small_name )
except Exception as e:
    print( e )
    print( goo.get() )

print( goo.get_private() )

print( goo.__class__ )

print( Goo.mro() )
print( Foo.mro() )

class Base():
    """docstring for Base"""
    def __init__(self):
        print( "S Base" )
        print( "E Base" )

class A( Base ):
    def __init__( self ):
        print( "S A" )
        super( A, self ).__init__()
        print( "E A" )


class B( Base ):
    def __init__( self ):
        print( "S B" )
        super( B, self ).__init__()
        print( "E B" )


class C( A, B ):
    def __init__( self ):
        print( "S C" )
        super( C, self ).__init__()
        print( "E C" )

C = C()

class One( Base ):
    def __init__( self ):
        print( "S One" )
        Base().__init__()
        print( "E One" )

class Two( Base ):
    def __init__( self ):
        print( "S Two" )
        Base().__init__()
        print( "E Two" )

class Three( One, Two ):
    def __init__( self ):
        print( "S Three" )
        One().__init__()
        Two().__init__()
        print( "E Three" )

Three = Three()

class static():
    """static"""
    @staticmethod
    def s_test(a, b):
        print( a * b )
    def test( self, a, b ):
        print( a + b )


s = static()
static.s_test(1, 9)
s.test(1, 9)

print( __name__ )
print( __import__ )
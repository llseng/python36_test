# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-20 10:56:44
# @LastEditors: llseng
# @LastEditTime: 2021-01-20 10:56:44
#

# @staticmethod 静态方法 

from math import sqrt

class Triangle():
    """
    三角形
    """
    
    @staticmethod
    def is_valid( a, b, c ):
        return a + b > c and a + c > b and b + c > a
    
    def __init__( self, a, b, c ):
        self.a = a
        self.b = b
        self.c = c
    
    @property
    def a( self ):
        return self._a
    
    @a.setter
    def a( self, a ):
        self._a = a
        
    @property
    def b( self ):
        return self._b
    
    @b.setter
    def b( self, b ):
        self._b = b
        
    @property
    def c( self ):
        return self._c
    
    @c.setter
    def c( self, c ):
        self._c = c
    
    def perimeter( self ):
        return self.a + self.b + self.c
    
    def area( self ):
        half = self.perimeter() / 2
        return sqrt( half * ( half - self.a ) * ( half - self.b ) * ( half - self.c ) )

if __name__ == "__main__":
    a, b, c = 5, 7, 9
    if Triangle.is_valid( a, b, c ):
        t = Triangle( a, b, c)
        print( t.perimeter() )
        print( t.area() )
    else:
        print( "%d %d %d 不能构成三角形" % (a,b,c) )



# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-18 14:31:19
# @LastEditors: llseng
# @LastEditTime: 2021-01-18 14:31:19
#

class Foo():
    """
    foo
    """
    __slots__ = ( '_name', '_age', '_len', '_high' )

    def __init__(self, name, age):
        """
        init
        """
        self.name = name
        self.age = age

    @property
    def name( self ):
        print( "get name" )
        return self._name
    
    @name.setter
    def name( self, name ):
        print( "set name" )
        self._name = name
    
    @property
    def age( self ):
        print( "get age" )
        return self._age
    
    @age.setter
    def age(self, age):
        print( "set age" )
        self._age = age

    def play( self ):
        if self.age > 10:
            return "%s 在玩游戏" % self.name
        else:
            return "%s 在玩沙子" % self.name
    
    @staticmethod
    def p( str ):
        print( str )

if __name__ == "__main__":
    foo = Foo( "张三", 12 )
    Foo.p( foo.play() )
    foo.age = 5
    Foo.p( foo.play() )

    foo._len = 180
    foo._high = 156
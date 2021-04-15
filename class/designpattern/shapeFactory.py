# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-04-15 14:41:51
# @LastEditors: llseng
# @LastEditTime: 2021-04-15 14:41:52
#
from abc import ABCMeta, abstractmethod
from random import randint

class Shape( metaclass=ABCMeta ):
    """
    形状
    """
    def __init__( self, name ):
        self._name = name
    @abstractmethod
    def drow( self ):
        pass

class CircleShape( Shape ):
    """
    圆
    """
    def __init__( self, girth ):
        self._girth = girth
        super().__init__('Circle')
    
    def drow( self ):
        return [self._name, self._girth]

class TriangleShape( Shape ):
    """
    三角形
    """
    def __init__( self, girth ):
        self._girth = girth
        super().__init__('Triangle')
    
    def drow( self ):
        return [self._name, self._girth]

class RectangleShape( Shape ):
    """
    矩形
    """
    def __init__( self, girth ):
        self._girth = girth
        super().__init__('Rectangle')
    
    def drow( self ):
        return [self._name, self._girth]

class ShapeFactory:
    """
    工厂
    """
    def __init__( self ):
        self._callables = {}
    
    @staticmethod
    def isCallable( c ):
        if not callable( c ):
            return False
        if c.__code__.co_argcount:
            return False
        return True

    def biud( self, key, func ):
        if not ShapeFactory.isCallable( func ):
            return False
        # setdefault 只设置一次
        # self._callables.setdefault(key, callable)
        self._callables[ key ] = func
        return True

    def apply( self, key ):
        if key not in self._callables.keys():
            return None
        return self._callables[ key ]()

if __name__ == "__main__":
    F = ShapeFactory()
    F.biud( 'Circle', lambda: CircleShape( randint(1, 100) ) )
    F.biud( 'Triangle', lambda: TriangleShape( randint(1, 100) ) )
    F.biud( 'Rectangle', lambda: RectangleShape( randint(1, 100) ) )
    
    print( F )
    a = F.apply( 'Circle' )
    b = F.apply( 'Triangle' )
    c = F.apply( 'Triangle' )
    d = F.apply( 'Rectangle' )
    e = F.apply( 'Rectangle' )
    
    print( a.drow(), b.drow(), c.drow(), d.drow(), e.drow() )
    print( id(a), id(b), id(c), id(d), id(e) )

    # print( Shape() )

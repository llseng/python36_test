# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-04-16 11:37:19
# @LastEditors: llseng
# @LastEditTime: 2021-04-16 11:37:19
#

from abc import ABCMeta, abstractmethod

class Shape( metaclass=ABCMeta ):
    """
    形状抽象类
    """
    @abstractmethod
    def drow( self ):
        pass

class ShapeDecorator( Shape, metaclass=ABCMeta ):
    """
    形状装饰器抽象类
    """
    @abstractmethod
    def __init__(self, shape):
        self._shape = shape

    @abstractmethod
    def drow( self ):
        self._shape.drow()

class CircleShape( Shape ):
    """
    圆
    """
    def __init__(self):
        self._name = "Circle"
        super().__init__()
    
    def drow(self):
        print( self._name, "drow." )

class TriangleShape( Shape ):
    """
    三角形
    """
    def __init__(self):
        self._name = "Triangle"
        super().__init__()
    
    def drow(self):
        print( self._name, "drow." )


class RectangleShape( Shape ):
    """
    矩形
    """
    def __init__(self):
        self._name = "Rectangle"
        super().__init__()
    
    def drow(self):
        print( self._name, "drow." )

class RedShapeDecorator( ShapeDecorator ):
    """
    红色装饰器
    """
    def __init__(self, shape):
        super().__init__(shape)
    
    def drow(self):
        super().drow()
        print( "red", self._shape )

if __name__ == "__main__":
    
    redCircleShape = RedShapeDecorator( CircleShape() )
    redTriangleShape = RedShapeDecorator( TriangleShape() )
    redRectangleShape = RedShapeDecorator( RectangleShape() )

    redCircleShape.drow()
    redTriangleShape.drow()
    redRectangleShape.drow()
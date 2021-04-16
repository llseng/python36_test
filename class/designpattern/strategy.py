# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-04-16 12:25:04
# @LastEditors: llseng
# @LastEditTime: 2021-04-16 12:25:04
#

from abc import ABCMeta, abstractmethod

class Strategy( metaclass=ABCMeta ):
    """
    策略抽象类
    """
    @abstractmethod
    def doOperation( self, num1, num2 ):
        pass

class OperationAdd( Strategy ):
    """
    加法策略
    """
    def doOperation(self, num1, num2):
        return num1 + num2

class OperationSub( Strategy ):
    """
    减法策略
    """
    def doOperation(self, num1, num2):
        return num1 - num2

class OperationMultiply( Strategy ):
    """
    乘法法策略
    """
    def doOperation(self, num1, num2):
        return num1 * num2

class Context:
    """
    上下文
    """
    def __init__(self, strategy):
        self._strategy = strategy
    
    def execute( self, num1, num2 ):
        return self._strategy.doOperation( num1, num2 )

if __name__ == "__main__":

    contextAdd = Context( OperationAdd() )
    contextSub = Context( OperationSub() )
    contextMultiply = Context( OperationMultiply() )

    print( contextAdd.execute( 10, 5 ) )
    print( contextSub.execute( 10, 5 ) )
    print( contextMultiply.execute( 10, 5 ) )

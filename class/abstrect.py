# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-20 17:16:57
# @LastEditors: llseng
# @LastEditTime: 2021-01-20 17:16:58
#

import abc

class Animal( object, metaclass = abc.ABCMeta ):
    """
    动物
    """
    def __init__( self, name ):
        self.name = name
    
    @abc.abstractmethod
    def say( self ):
        pass

    def sayName( self ):
        print( "my name is", self.name )

class Cat( Animal ):
    """
    猫
    """
    def say( self ):
        print( "喵喵喵", self.name )

class Dog( Animal ):
    """
    狗
    """
    def say( self ):
        print( "汪汪汪", self.name )

if __name__ == "__main__":
    print( abc.ABC.__mro__ )
    c = Cat( 'Tom' )
    c.say()
    c.sayName()
    d = Dog( 'Hapa' )
    d.say()
    d.sayName()
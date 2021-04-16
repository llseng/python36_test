# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-04-16 14:34:02
# @LastEditors: llseng
# @LastEditTime: 2021-04-16 14:34:03
#

from abc import ABCMeta, abstractmethod

class Image( metaclass=ABCMeta ):
    """
    图片抽象类
    """
    
    @abstractmethod
    def __init__(self, filename):
        pass

    @abstractmethod
    def display( self ):
        pass

class RealImage( Image ):
    """
    真图片
    """
    def __init__(self, filename):
        self._filename = filename
        self.loadFromDisk()
    
    def display(self):
        print( "Displaying", self._filename )

    def loadFromDisk(self):
        print( "loading", self._filename )

class ProxyImage( Image ):
    """
    图片代理
    """
    def __init__(self, filename):
        self._filename = filename
        self._realimage = None
    
    def display(self):
        if self._realimage is None:
            self._realimage = RealImage( self._filename )
        self._realimage.display()

if __name__ == "__main__":
    
    proxy = ProxyImage( "imgimgimg.png" )
    real = RealImage( "imgimgimg.png" )

    proxy.display()
    real.display()
    print( "以下无需初始化" )
    proxy.display()
    real.display()

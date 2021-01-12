# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-11 15:09:52
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-11 15:13:04

name = 'python'

def test( ):
    name = "test"
    def test():
        nonlocal name
        name = "inner_test"
        print( name )
    test()
    print( name )

test()
print( name )
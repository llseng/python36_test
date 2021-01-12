# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-11 11:47:04
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-11 11:52:08

def test( a, b ):
    try:
        result = a / b
        raise Exception( 'test raise' )
    except (ZeroDivisionError, Exception ) as e:
        print( e )
    else:
        print( result )
    finally:
        print( 'finally' )

test( 1, 0 )
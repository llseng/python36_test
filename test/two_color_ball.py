# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-06-16 11:41:28
# @LastEditors: llseng
# @LastEditTime: 2021-06-16 11:41:29
#
from sys import argv
from random import choice, sample
from getopt import getopt, GetoptError

def usage():
    print("""
-n, --num   <data>  :num (default 1)
-f                  :FC (default)
-t                  :TC
-h                  :help
""")
    exit()

def Two_ball(rlen, rnum, blen, bnum):
    '''
    :param rlen: 红球长度
    :param rnum: 红球个数
    :param blen: 蓝球长度
    :param bnum: 蓝球个数
    :return: ([红球...], [蓝球...])
    '''
    
    red_balls = [ x + 1 for x in range( rlen ) ]
    blue_balls = [x + 1 for x in range( blen ) ]

    rres = sample( red_balls, rnum )
    rres.sort()
    bres = sample( blue_balls, bnum )
    bres.sort()
    
    return rres, bres

def TC_two_ball():
    return Two_ball(35, 5, 12, 2)

def FC_two_ball():
    return Two_ball(33, 6, 16, 1)

if __name__ == '__main__':
    try:
        opts, args = getopt(argv[1:], 'htfn:', ['--num='])
    except GetoptError as err:
        print(err)
        usage()

    # 函数指针
    tb_def = FC_two_ball
    # 调用次数
    num = 1

    for o, a in opts:
        if o == '-h':
            usage()
        elif o == '-t':
            tb_def = TC_two_ball
        elif o in ('-n', '--num'):
            num = int( a )
            if num < 1: num = 1
        else:
            pass

    for x in range( num ):
        tb = tb_def()
        print( tb[0], tb[1] )

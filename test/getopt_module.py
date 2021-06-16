# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-06-16 14:59:37
# @LastEditors: llseng
# @LastEditTime: 2021-06-16 14:59:37
#

from getopt import getopt, GetoptError 

def usage():
    s = """
-f, --file <data>   文件名
-d, --debug         开启调试
-v, --version       版本号
-h, -?, --help      帮助
    """
    print(s)

if __name__ == '__main__':
    s = "-h --debug -v --file=t.log"
    argv = s.split()
    try:
        opts, args = getopt(argv, 'h?vdf:', ['debug', 'help', 'file=', 'version'] )
    except GetoptError as err:
        print(err)
        usage()
        exit()
    
    for o, a in opts:
        if o in ('-h', '-?', '--help'):
            usage()
            exit()
        elif o in ('-v', '--version'):
            print('Version: 1.0.0')
            exit()
        elif o in ('-d', '--debug'):
            print('debug debug debug debug debug')
        elif o in ('-f', '--file'):
            print('文件名:', a)
        else:
            # assert False, 'unhandled option'
            print(o, a)
# -*- coding: utf-8 -*-
# @Descripttion:
# @version:
# @Author: llseng
# @Date: 2021-01-13 15:16:22
# @LastEditors: llseng
# @LastEditTime: 2021-01-13 15:34:43
#

import threading, time

i = 100
i_lock = threading.Lock()

def print_i(name):
    global i
    while i > 0:
        use_lock = i_lock.acquire(True, 1)
        while not use_lock:
            print(name, 'not use_lock')
            # time.sleep( 0.1 )
            use_lock = i_lock.acquire(True, 1)

        i -= 1
        print(name, i)
        # print(name, 'sleep 1')
        # time.sleep( 1 )

        i_lock.release()

threading.Thread( target=print_i, args=('lt1',) ).start()
threading.Thread( target=print_i, args=('lt2',) ).start()
threading.Thread( target=print_i, args=('lt3',) ).start()
threading.Thread( target=print_i, args=('lt4',) ).start()


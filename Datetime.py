# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-11 18:46:09
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-11 19:07:42

import time, calendar

print( 'time.perf_counter()', time.perf_counter() )
print( 'time.process_time()', time.process_time() )

now_time = time.time()

print( '时间搓', int( time.time() ), now_time ) 

print( '获取当前时间', time.localtime( ) )
print( '获取当前时间', time.localtime( now_time ) )

print( '格式化当前时间' )
print( 'asctime:', time.asctime( time.localtime() ) )
print( 'strftime:' )
print( '"%Y-%m-%d %H:%M:%S"', time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() ) )

print( '日历' )
print( calendar.month(2021, 1) )

time.sleep( 1 )

print( 'time.perf_counter()', time.perf_counter() )
print( 'time.process_time()', time.process_time() )

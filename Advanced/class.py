# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-26 10:52:08
# @LastEditors: llseng
# @LastEditTime: 2021-01-26 10:52:09
#

import asyncio, aiohttp, re

# 协程简单实例

def tmp_server( ):
    count = 0
    while True:
        value = yield count
        count += 1
        print( "处理", value, count )

s = tmp_server()
next( s ) # 初始化(必须) 
print( s.send( 10 ) )
print( s.send( 20 ) )
print( s.send( 30 ) )

# 异步I/O模块

async def prime_filter( n, m ):
    primes = []
    for i in range( n, m + 1 ):
        flag = True
        for j in range( 2, int( i ** 0.2 + 1 ) ):
            if i % j:
                flag = False
                break

        if flag:
            print( "Prime =>", i )
            primes.append( i )

        await asyncio.sleep( 0.001 )
    return tuple( primes )

async def square_mapper( n, m ):
    squares = []
    for i in range( n, m + 1 ):
        print( "square =>", i * i )
        squares.append( i * i )

        await asyncio.sleep( 0.001 )
    
    return squares

def main():
    
    loop = asyncio.get_event_loop()
    future = asyncio.gather( prime_filter( 1, 20 ), square_mapper( 1, 20 ) )
    future.add_done_callback( lambda x: print( x, x.result() ) )
    loop.run_until_complete( future )
    # loop.close()

main()

title_regx = re.compile( r"\<title\>(?P<title>.*)\<\/title\>" )

async def fetch_page( session, url ):
    async with session.get( url, ssl=False ) as resp:
        return await resp.text()

async def show_title( url ):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page( session, url )
        t_search = title_regx.search( html ),
        print( t_search )

def main2():
    urls = [
        'https://www.python.org/',
        'https://git-scm.com/',
        'https://www.jd.com/',
        'https://www.taobao.com/',
        'https://www.douban.com/'
    ]

    loop = asyncio.get_event_loop()
    cos = [ show_title( url ) for url in urls ]
    loop.run_until_complete( asyncio.wait( cos ) )
    loop.close()

main2()
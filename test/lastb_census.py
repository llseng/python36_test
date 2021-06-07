# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-06-05 12:25:32
# @LastEditors: llseng
# @LastEditTime: 2021-06-05 12:27:00
#

import os, json, pickle, heapq, matplotlib.pyplot as plt
from os import path

def getLastbData(file_path):
    if not path.isfile( file_path ): return None
    lastb_data = {}
    ips = {}
    num = 0

    with open( file_path, mode="r" ) as fd:
        for line in fd.readlines():
            l = line.split()
            if len( l ) != 10: continue

            # if l[0] not in lastb_data:
            #     lastb_data[ l[0] ] = {'num': 0, 'ips':{}}
            lastb_data.setdefault( l[0], {'num': 0, 'ips':{}} )
            lastb_data[ l[0] ][ 'num' ] += 1
            # if l[2] not in lastb_data[ l[0] ][ 'ips' ]:
            #     lastb_data[ l[0] ][ 'ips' ][ l[2] ] = 0
            lastb_data[ l[0] ][ 'ips' ].setdefault( l[2], 0 )
            lastb_data[ l[0] ][ 'ips' ][ l[2] ] += 1

            ips.setdefault( l[2], 0 )
            ips[ l[2] ] += 1

            num += 1

    return [lastb_data, ips, num]

if __name__ == "__main__":

    # username: {num: 0, ips: {}}
    data = {}
    
    pkl_path = path.join( path.dirname( __file__ ), "lastb_log.pkl" )
    file_path = path.join( path.dirname( __file__ ), "lastb_log.log" )

    if not path.isfile( pkl_path ):
        with open(pkl_path, mode="wb") as pfd:
            pickle.dump(getLastbData(file_path), pfd)

    with open(pkl_path, mode="rb") as fd:
        data = pickle.load(fd)

    lastb_data = data[0]
    ips = data[1]
    num = data[2]

    # 饼状图

    # Tops = heapq.nlargest(20, lastb_data.items(), lambda x: x[1]['num'])
    # labels = []
    # sizes = []
    # explode = []

    # other_num = num
    # for t in Tops:
    #     if t[0] == "root": continue
    #     labels.append( t[0] )
    #     sizes.append( t[1]['num'] )
    #     if t[0] == "root":
    #         explode.append( 0.1 )
    #     else:
    #         explode.append( 0 )
    #     other_num -= t[1]['num']
    
    # # labels.append( 'other' )
    # # sizes.append( other_num )
    # # explode.append( 0 )

    # fig1, ax1 = plt.subplots()
    # ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    # ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # plt.show()

    # 饼状图结束

    # 打印用户名

    # Tops = heapq.nlargest(100, lastb_data.items(), lambda x: x[1]['num'])
    # for x in Tops:
    #     print( x[0], x[1]['num'] )

    # Bots = heapq.nsmallest(100, lastb_data.items(), lambda x: x[1]['num'])
    # for x in Bots:
    #     print( x[0], x[1]['num'] )

    # 打印用户名结束
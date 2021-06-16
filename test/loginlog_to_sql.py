# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-06-10 16:16:07
# @Last Modified by:   llseng
# @Last Modified time: 2021-06-10 18:11:32

import sys, os, re, json

def deal_sql( line ):
    res = re.findall( r'\[(.+?)\].+(\{.+\})', line )
    if not res: return

    date = res[0][0]
    data = json.loads( res[0][1] )
    sql = f'insert into tb_player (`playerid`,`reg_time`,`nick`,`accountId`,`serverid`,`channel`,`agentid`,`upplayerid`,`type`,`scene`,`session_key`,`platform`,`shareid`,`photo`,`reg_ip`,`province_id`,`openid`) values ("{ data["playerid"] }","{ date }","{ data["nick"] }","{ data["unionid"] }","ww01","cjkg","","0","20","0","","0","0","","223.104.45.51","0","{ data["openid"] }");'
    return sql

if __name__ == '__main__':

    if len( sys.argv ) < 2:
        print( 'No file selected' )
        exit()

    fpath = os.path.join( os.path.dirname( __file__ ), sys.argv[1] )
    if not os.path.isfile( fpath ):
        print( 'It\'s not a file', fpath )
        exit()

    with open( fpath, mode='r' ) as fd:
        for line in fd.readlines():
            print( deal_sql( line ) )


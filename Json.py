# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-11 18:41:00
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-11 18:44:53

import json

data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com',
    'list' : [ 12135, 65418, 16654498, 15 ],
    'tuple' : ( '12135', '65418', '16654498', '15' )
}

print( json.loads( '{"sodar_query_id":"jSv8X8mqFoaA9AWvm4O4CQ","injector_basename":"sodar2","bg_hash_basename":"PbZvCEkorD5rxjWOexle1_regFmuc5-vrUA2zacPm4s"}' ) )
print( json.dumps( data ) )
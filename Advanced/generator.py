# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-23 14:25:39
# @LastEditors: llseng
# @LastEditTime: 2021-01-23 14:25:39
#

tmp_dict = {
    'upgrade':1,
    'building':1,
    'sign_in':1,
    'newcomer':1,
    'cumulation_ad':1,
    'task':1,
    'secretary':1,
    'cumulation_ad_1':1,
    'pet_grade':1,
    'upgrade_building':0,
    'turntable':50,
    'turntable_0':50,
    'turntable_count_1':100,
    'online_re':100,
    'online_1':200,
    'lattice':500,
    'lattice_1':100,
    'live_show_1':500,
    'today_task':100,
    'new_online_0':50,
}

tmp_keys = [x for x in tmp_dict.keys() if not x[-1].isnumeric()]

print( tmp_keys )

tmp_dict2 = {k:v for k,v in tmp_dict.items() if not k[-1].isnumeric() }
print( tmp_dict2 )

tmp_dict3 = {k:v for k,v in tmp_dict.items() if k[-1].isnumeric() }
print( tmp_dict3 )

tmp_dict4 = {k:v for k,v in tmp_dict.items() if v > 1 }
print( tmp_dict4 )

tmp_dict5 = {k:v for k,v in tmp_dict.items() if v > 100 }
print( tmp_dict5 )

tmp_dict6 = {k:v for k,v in tmp_dict.items() if v == 1 }
print( tmp_dict6 )

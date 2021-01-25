# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-23 18:40:48
# @LastEditors: llseng
# @LastEditTime: 2021-01-23 18:40:49
#

import glob

print( glob.glob( "*/*.py" ) )

print( sorted( glob.glob( "*py" ) ) )
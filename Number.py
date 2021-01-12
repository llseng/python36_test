# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-09 11:32:30
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-09 19:15:29

import random

a = 19
b = 18

print( "a = %d, b = %d" % (a, b) )
print( "a > b %d" % (a > b) )
print( "a / b %f" % (a / b) )
print( "a // b %f" % (a // b) )
print( a % (b-6) )

print( "rand %f" % (random.random() * 100) )
print( "rand %f" % round(random.random() * 100, 0) )

i = int( random.random() * 100 )

for x in range(1,1000):
    if random.random() > 0.5:
        i += 0.5
    else:
        i -= 0.5
    print( i )
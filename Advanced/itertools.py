# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-23 16:33:49
# @LastEditors: llseng
# @LastEditTime: 2021-01-23 16:33:49
#

import itertools

# 产生ABCD的全排列
t1 = itertools.permutations('ABCD')
# 产生ABCDE的五选三组合
t2 = itertools.combinations('ABCDE', 3)
# 产生ABCD和123的笛卡尔积
t3 = itertools.product('ABCD', '123')
# 产生ABC的无限循环序列
t4 = itertools.cycle(('A', 'B', 'C'))

i = 0
for x in t1:
    if i > 10: break
    print( x, end= ', ' )
    i += 1
print()

i = 0
for x in t2:
    if i > 10: break
    print( x, end= ', ' )
    i += 1
print()

i = 0
for x in t3:
    if i > 10: break
    print( x, end= ', ' )
    i += 1
print()

i = 0
for x in t4:
    if i > 10: break
    print( x, end= ', ' )
    i += 1
print()
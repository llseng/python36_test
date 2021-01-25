# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-23 15:49:00
# @LastEditors: llseng
# @LastEditTime: 2021-01-23 15:49:00
#

names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']

# 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# 错误按例  可变参数 复制 只是引用 并不会开辟内存
# scores =  [ [ None ] * len( courses ) ] * len(names)
scores = [[None] * len(courses) for _ in range(len(names))]

print( scores )

for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
        print(scores)
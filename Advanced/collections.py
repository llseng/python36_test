# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-25 14:31:35
# @LastEditors: llseng
# @LastEditTime: 2021-01-25 14:31:35
#

import collections 

# 类工厂
Parr = collections.namedtuple( 'Parr', "head last list len" )

print( Parr )

parray = Parr( last='e', head='a', list='abcde', len=5 )

print( parray )
print( parray._fields )
print( parray.list )
print( parray._asdict() )

print( parray._replace( list="ABCDE" ) ) 
print( parray )
print( parray._asdict() )

# 双向队列
deque_queue = collections.deque( )
print( deque_queue )
deque_queue.append( 1 )
deque_queue.append( 2 )
deque_queue.append( 3 )
deque_queue.appendleft( 4 )
deque_queue.appendleft( 5 )
deque_queue.appendleft( 6 )

print( deque_queue )

deque_queue.pop()
deque_queue.pop()
deque_queue.popleft()
deque_queue.popleft()

print( deque_queue )
deque_queue.extend( [55,5644,4,46] )
print( deque_queue )

deque_queue.extendleft( ['a', 'b', 'c', 'd'] )
print( deque_queue )

# 元素计数器

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = collections.Counter(words)

print( counter )
print( counter.most_common(3) )
print( counter.elements() )

# orderedDict 
ODict = collections.OrderedDict()
Dict = {}
print( ODict )
print( Dict )

ODict['name'] = 'test'
ODict['age'] = 22
ODict['len'] = 180
ODict['c'] = 1
ODict['b'] = 2
ODict['a'] = 3

Dict['name'] = 'test'
Dict['age'] = 22
Dict['len'] = 180
Dict['c'] = 1
Dict['b'] = 2
Dict['a'] = 3

print( ODict )
print( Dict )

for k,v in ODict.items():
    print('ODict', k, v )

for k,v in Dict.items():
    print('Dict', k, v )

print( Dict.get('name2') )
print( Dict.get('name2', 'null') )

# defaultDict
defDict = collections.defaultdict( int )
print( defDict )
print( defDict['name'] )
print( defDict.get('name') )
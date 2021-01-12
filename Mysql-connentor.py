# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-11 17:43:47
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-11 18:32:20

import mysql.connector

mydb = mysql.connector.connect(
        host = '192.168.0.200',
        user = 'root',
        passwd = '123456',
        database = 'test'
    );

print( mydb )
print( mydb.connection_id )
print( mydb.database )
print( mydb.autocommit )

query = mydb.cursor( );

print( query )

sql = 'show databases'
print( '-----', sql )
query.execute( sql )
print( query.rowcount )

for line in query:
    print( line )

sql = 'show tables'
print( '-----', sql )
query.execute( sql )
print( query.rowcount )

for line in query:
    print( line )

sql = 'show create table student'
print( '-----', sql )
query.execute( sql )
print( query.rowcount )

for line in query:
    print( line )

sql = 'select * from student'
print( '-----', sql )
query.execute( sql )
print( query.description )
print( query.rowcount )

for line in query:
    print( line )

sql = 'insert into student( name, age ) values( %s, %s )'
print( '-----', sql % ('mydb' + str( mydb.connection_id ), str( mydb.connection_id ) ) )
query.execute( sql, ('mydb' + str( mydb.connection_id ), mydb.connection_id) )
mydb.commit()

print( query.lastrowid )
print( query.rowcount )


sql = 'delete from student where id = %s'
print( '-----', sql % (str( query.lastrowid )) )
query.execute( sql % ( str( query.lastrowid ) ) )
mydb.commit()

print( query.lastrowid )
print( query.rowcount )

sql = 'select * from student order by id desc'
print( '-----', sql )
query.execute( sql )

for line in query:
    print( line )

# print( query.description )
# print( query.lastrowid )
# print( query.rowcount )

mydb.close()
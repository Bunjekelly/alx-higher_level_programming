#!/usr/bin/python3

"""a script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connect = MySQLdb.connect(host="localhost", user=username, passwd=password,
                              db=database, port=3306)

cursor = connect.cursor()

cursor.execute("SELECT * FROM states WHERE name\
               LIKE BINARY 'N%' ORDER BY id ASC")

result = cursor.fetchall()

for i in result:
    print(i)

cursor.close()
connect.close()

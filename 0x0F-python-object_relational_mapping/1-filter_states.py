#!/usr/bin/python3

"""a script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa"""

import MySQLdb

db = MySQLdb.connect(host="localhost", user="root",
                     passwd="b_techie", db="hbtn_0e_0_usa", port=3306)

cursor = db.cursor()

cursor.execute("SELECT * FROM states WHERE name
               LIKE BINARY 'N%' ORDER BY id ASC")

result = cursor.fetchall()

for i in result:
    print(i)

db.close()

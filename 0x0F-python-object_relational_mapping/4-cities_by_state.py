#!/usr/bin/python3

"""a script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb

db = MySQLdb.connect(host="localhost", user="root",
                     passwd="b_techie", db="hbtn_0e_4_usa", port=3306)

cursor = db.cursor()

cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC")

result = cursor.fetchall()

for i in result:
    print(i)

db.close()

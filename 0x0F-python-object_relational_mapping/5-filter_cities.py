#!/usr/bin/python3

"""a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""

import sys
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root",
                     passwd="b_techie", db="hbtn_0e_4_usa", port=3306)

cursor = db.cursor()

state = sys.argv[4]

cursor.execute("SELECT cities.name FROM cities \
               JOIN states ON cities.state_id = states.id \
               WHERE states.name = %s ORDER BY cities.id ASC;", (state,))

result = cursor.fetchall()

for i in result:
    print(i)

db.close()

#!/usr/bin/python3

""" a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument."""

import sys
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root",
                     passwd="b_techie", db="hbtn_0e_0_usa", port=3306)

cursor = db.cursor()

state = sys.argv[4]

cursor.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
                   ORDER BY id ASC""".format(state))

result = cursor.fetchall()

for i in result:
    print(i)

db.close()

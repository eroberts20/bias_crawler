#!/usr/bin/python
import mysql.connector



# you must create a Cursor object. It will let
#  you execute all the queries you need

# Use all the SQL you like

# print all the first cell of all the rows
def get_bias(url):
    db = mysql.connector.connect(host="localhost", user="eroberts20", passwd="342normal", db="newsdb")        # name of the data base
    cur = db.cursor()
    cur.execute("SELECT * FROM sites")


    for row in cur.fetchall():

        if row[0] in url:
            return row[1]
        db.close()

    return 0;

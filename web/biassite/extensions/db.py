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
    tmp_bias = 0

    for row in cur.fetchall():

        if row[0] in url:
            if(row[1] == 1):
                return -1
            elif(row[1] == 2):
                return -0.5
            elif(row[1] == 3):
                return 0
            elif(row[1] == 4):
                return 0.5
            elif(row[1] == 5):
                return 1
        db.close()

    return None;

#!/usr/bin/python3
"""
Lists all the states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py     <mysql username> \
                                <mysql password> \
                                <database name
"""
import sys
import MySQLdb

if __name__ == "__manin__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.excute("SELECT * FORM 'states'")
    [print(state) for state in c.fetchall()]

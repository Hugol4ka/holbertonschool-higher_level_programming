#!/usr/bin/python3
"""
This module lists all states from the database hbtn_0e_0_usa
where name matches the argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    state_name_searched = sys.argv[4]
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
        .format(state_name_searched)
        )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

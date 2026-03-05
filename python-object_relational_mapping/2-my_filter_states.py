#!/usr/bin/python3
"""
This is a module-level docstring.
It describes the purpose of the entire script/module.
"""


import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8")
    cur = conn.cursor()
    q = "SELECT * " \
        "FROM states WHERE name='{}' " \
        "ORDER BY id ASC".format(sys.argv[4])
    cur.execute(q)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

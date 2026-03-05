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
    q = """SELECT
            cities.name
        FROM cities
            INNER JOIN states
            ON states.id=cities.state_id
        WHERE states.name = %(name)s
        ORDER BY cities.id ASC"""
    cur.execute(q, {"name": sys.argv[4]})
    query_rows = cur.fetchall()
    list_cities = [row[0] for row in query_rows]
    print(", ".join(list_cities))
    cur.close()
    conn.close()

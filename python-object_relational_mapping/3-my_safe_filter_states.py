#!/usr/bin/python3
"""Get all states """
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306, user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE
                name = '%s' ORDER BY id ASC", (state_name,))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()

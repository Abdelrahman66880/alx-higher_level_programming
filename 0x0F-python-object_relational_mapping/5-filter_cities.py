#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    myconn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = myconn.cursor()
    uin = sys.argv[4]
    cursor.execute("""SELECT cities.name FROM cities INNER JOIN states
                   ON cities.state_id = states.id
                   WHERE states.name = %s""", (uin, ))
    rows = cursor.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cursor.close()
    myconn.close()

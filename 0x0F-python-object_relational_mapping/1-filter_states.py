#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":

    myconn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    mycursor = myconn.cursor()

    mycursor.execute("""
    SELECT *
    FROM states
    WHERE name LIKE BINARY 'N%'
    ORDER BY states.id
    """)

    results = mycursor.fetchall()

    for i in results:
        print(i)

    myconn.commit()
    myconn.close()

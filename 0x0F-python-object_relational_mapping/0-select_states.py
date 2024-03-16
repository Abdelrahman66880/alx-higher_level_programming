import MySQLdb
import sys

if __name__ == "__main__":

    myconn = MySQLdb.connect(host = "localhost", user = sys.argv[1], 
                             passwd = sys.argv[2], database = sys.argv[3], port = 3306)

    mycursur = myconn.cursor()
    mycursur.execute("SELECT * FROM states")

    results = mycursur.fetchall()

    for i in results:
        print(i)

    myconn.commit()
    myconn.colse()

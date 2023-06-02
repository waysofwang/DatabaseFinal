# connect_try.py
import mysql.connector as mq
from mysql.connector import errorcode
try:
    conn = mq.connect(host='localhost', user='root', password='YU_oppdivide!20', db='pythonsql')
    print("Connected")

except mq.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print("Connection closed")
    conn.close()

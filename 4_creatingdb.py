import mysql.connector

# Establish connection to the MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YU_oppdivide!20"
)

if connection.is_connected():
    print("Connected to MySQL server")


    cursor = connection.cursor()

    # Drop the menagerie database if it exists
    cursor.execute("DROP DATABASE IF EXISTS menagerie")

    cursor.execute("CREATE  DATABASE  menagerie")

    # Close the cursor and the connection
    cursor.close()
    connection.close()
    print("Disconnected from MySQL server")
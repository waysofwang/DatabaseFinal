import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YU_oppdivide!20"
)

if connection.is_connected():
    print("You have Connected to MySQL server")

    # Create a cursor object
    cursor = connection.cursor()

    # Drop the menagerie database if it exists
    cursor.execute("DROP DATABASE IF EXISTS menagerie")

    # Close the cursor and the connection
    cursor.close()
    connection.close()
    print("Disconnected from MySQL server")
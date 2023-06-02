import mysql.connector as mc

# Establish a connection to the MySQL server
conn = mc.connect(
    host='localhost',
    user='root',
    password='YU_oppdivide!20',
    db='menagerie'
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute the SELECT query
query = "SELECT * FROM pet"
cursor.execute(query)

# Fetch all the rows from the result set
rows = cursor.fetchall()

# Display the data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()

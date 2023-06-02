import mysql.connector as mc
from tabulate import tabulate

# Establish a connection to the MySQL server
conn = mc.connect(
    host='localhost',
    user='root',
    password='YU_oppdivide!20',
    database='menagerie'
)

def get_female_dogs():
    cursor = conn.cursor()
    query = "SELECT * FROM pet WHERE species = 'dog' AND sex = 'f'"
    cursor.execute(query)
    pet_records = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print(tabulate(pet_records, headers=headers, tablefmt="fancy_grid"))

def main():
    get_female_dogs()
    conn.close()

if __name__ == '__main__':
    main()

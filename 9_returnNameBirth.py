import mysql.connector as mc
from tabulate import tabulate

# Establish a connection to the MySQL server
conn = mc.connect(
    host='localhost',
    user='root',
    password='YU_oppdivide!20',
    database='menagerie'
)

def get_name_and_birth():
    cursor = conn.cursor()
    query = "SELECT name, birth FROM pet"
    cursor.execute(query)
    pet_records = cursor.fetchall()
    headers = ['Name', 'Birth']
    print(tabulate(pet_records, headers=headers, tablefmt="fancy_grid"))

def main():
    get_name_and_birth()
    conn.close()

if __name__ == '__main__':
    main()

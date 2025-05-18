# This program demonstrates using UPDATE queries in python.
import sqlite3

# Connect to the database and create the cursor object
connection = sqlite3.connect('users.db')
cursor = connection.cursor()

def print_database():
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()

    for record in data:
        print(record)

update_query = """
UPDATE users SET password = ?, age = ? 
WHERE username = ?"""

cursor.execute(update_query, ('newpassword12345', 42, 'alicej'))
connection.commit()

print_database()
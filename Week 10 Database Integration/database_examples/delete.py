# This program demonstrates using UPDATE queries in python.
import sqlite3

# Connect to the database and create the cursor object
connection = sqlite3.connect('users.db')
cursor = connection.cursor()

# Simple function to print each record in the table.
def print_database():
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()

    for record in data:
        print(record)

# DELETE query and id number of the user to delete
delete_query = 'DELETE FROM users WHERE id = ?'
id = (1,)

# Execute and commit the query.
cursor.execute(delete_query, id)
connection.commit()

# Print the updated database
print_database()
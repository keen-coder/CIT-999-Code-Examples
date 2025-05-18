# This program demonstrates examples of executing INSERT queries.

import sqlite3

# Connect to the database and create a cursor object
connection = sqlite3.connect('users.db')
cursor = connection.cursor()

# Simple function to print each record in the table.
def print_database():
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()

    for record in data:
        print(record)

# Insert a single user
insert_query = '''
INSERT INTO users (first_name, last_name, age, street, city, state, zipcode, phone, username, password)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''

user_data = ("Nina", "Bennett", 31, "12 Redwood Trail", "Boulder", "CO", "80301",
             "720-555-1122", "ninab", "sunset21")

# Execute and commit the insert query
cursor.execute(insert_query, user_data)
connection.commit() # Commit the query to the database.

# Insert multiple new users
new_users = [
    ("Brian", "Smith", 34, "456 Oak Ave", "Lincoln", "NE", "68508", "555-5678", "brians", "mypassword"),
    ("Chloe", "Martinez", 22, "789 Pine Dr", "Madison", "WI", "53703", "555-9012", "chloem", "pass123"),
    ("David", "Nguyen", 45, "321 Elm Blvd", "Austin", "TX", "73301", "555-3456", "davidn", "qwerty456")
]

cursor.executemany(insert_query, new_users)
connection.commit()

# Print the results
print_database()
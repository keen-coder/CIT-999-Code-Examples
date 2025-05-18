import sqlite3 # builtin python module to handle connections and queries for SQLite databases

# Connect to the SQLite database file. The file path is relative to the current working directory
connection = sqlite3.connect("users.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Execute a query to select all records from the database.
# REMEMBER: This does NOT return the results.
cursor.execute('SELECT * from users')

# Fetch the results of the previous query.
# The results are returned as a list of tuples.
results = cursor.fetchall()

# Display the results
for record in results:
    print(record)
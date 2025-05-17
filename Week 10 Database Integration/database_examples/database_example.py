import sqlite3 # builtin python module to handle connections and queries for SQLite databases
from user import User

# Connecting to a Database--------------------------------------------------------------------------

# Connect to the SQLite database file. The file path is relative to the current working directory
connection = sqlite3.connect("users.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# --------------------------------------------------------------------------------------------------

# Executing a Query---------------------------------------------------------------------------------

# Run a query to select all records from the database.
cursor.execute('SELECT * from users')

# --------------------------------------------------------------------------------------------------

# Fetching the Results------------------------------------------------------------------------------

# Fetch the results from the query previously executed. The data is returned as a list of
# tuples where each record is a tuple in the list.
results = cursor.fetchall()

# --------------------------------------------------------------------------------------------------

# Display the Results-------------------------------------------------------------------------------

# Display all the data
for record in results:
    print(record)

# --------------------------------------------------------------------------------------------------

# Bonus: Fetch all results where the user's age is >= 40, store each record in a User object.-------

# Execute a new query and fetch the results
cursor.execute('SELECT * from users WHERE age >= ?', (40,))
results = cursor.fetchall()

user_list = []

# Parse the results into objects.
for record in results:
    first_name = record[1]
    last_name = record[2]
    age = record[3]
    street = record[4]
    city = record[5]
    state = record[6]
    zipcode = record[7]
    phone = record[8]
    username = record[9]
    password = record[10]

    new_user = User(first_name, last_name, age, street, city, state,
                    zipcode, phone, username, password)

    user_list.append(new_user)

# Display the objects
for user in user_list:
    print(user)

# --------------------------------------------------------------------------------------------------
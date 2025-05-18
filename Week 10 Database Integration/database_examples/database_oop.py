# This example shows how you could convert the database results into a list of objects.
import sqlite3
from user import User

# Connect to the database and create the cursor object
connection = sqlite3.connect('users.db')
cursor = connection.cursor()

# NOTE 1: Queries can also be stored as a separate string.
# NOTE 2: The use of ? here is called a parameterized query, we cover this later in the lecture.
select_query = 'SELECT * from users WHERE age >= ?'
age = (40,) # Parameterized queries require that the data be sent as a tuple even if there is only
            # one value.

# Execute the query and fetch the results.
cursor.execute(select_query, age)
results = cursor.fetchall()

user_list = []

# Parse the results into objects.
# NOTE: Keep in mind, each record is a tuple so we can use python's iterable unpacking functionality
#   to assign each value to its respective variable.
for record in results:

    # Unpack the record into individual values
    id, first_name, last_name, age, street, city, state, zipcode, phone, username, password = record

    # Create the new User object using the previous values.
    new_user = User(first_name, last_name, age, street, city, state,
                    zipcode, phone, username, password)

    # Add the new user to the end of the list.
    user_list.append(new_user)

# Display the objects
for user in user_list:
    print(user)
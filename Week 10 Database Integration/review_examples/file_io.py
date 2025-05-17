import csv

# Function to read the user information from the file and return a list
# of dictionaries, where each dictionary contains the user information.
def read_data(file_name):
    users = []

    # Read the data from the csv file.
    with open('users.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user = {
                'name': row['name'],
                'age': int(row['age']),
                'address': {
                    'street': row['street'],
                    'city': row['city'],
                    'state': row['state']
                },
                'phone': row['phone'],
                'username': row['username'],
                'password': row['password']
            }
            users.append(user)

    return users

# Function to display all user information
def display_users(users):
    print('User Directory:')
    print('-' * 50)
    for user in users:
        addr = user['address']
        print(f'Name     : {user['name']}')
        print(f'Age      : {user['age']}')
        print(f'Address  : {addr['street']}, {addr['city']}, {addr['state']}')
        print(f'Phone    : {user['phone']}')
        print(f'Username : {user['username']}')
        print(f'Password : {user['password']}')
        print('-' * 50)

def add_user(users, name, age, street, city, state, phone, username, password):
    new_user = {
            'name': name,
            'age': age,
            'address': {
                'street': street,
                'city': city,
                'state': state
            },
            'phone': phone,
            'username': username,
            'password': password
        }

    users.append(new_user)

def write_data(file_name, users):
    # Define fieldnames for CSV output
    fieldnames = ['name', 'age', 'street', 'city', 'state', 'phone', 'username', 'password']

    # Write all users to a new CSV file
    with open('users_updated.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for user in users:
            writer.writerow({
                'name': user['name'],
                'age': user['age'],
                'street': user['address']['street'],
                'city': user['address']['city'],
                'state': user['address']['state'],
                'phone': user['phone'],
                'username': user['username'],
                'password': user['password']
            })



if __name__ == '__main__':
    users = read_data('users.csv')
    display_users(users)

    add_user(users, 'Jessica', 27, '456 Elm St',
             'Rivertown', 'CA', '555-1111',
             'aliceb', 'alice123')

    add_user(users, 'David', 34, '789 Oak St',
             'Hillview', 'TX', '555-2222',
             'dgreen','green456',)

    write_data('users_updated.csv', users)
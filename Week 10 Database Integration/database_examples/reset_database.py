# Utility program to reset the database back to its original data.

import sqlite3

# Connect to the database and create a cursor object.
connection = sqlite3.connect('users.db')
cursor = connection.cursor()

# DELETE all rows from the users table
cursor.execute('DELETE FROM users')
cursor.execute('DELETE FROM sqlite_sequence WHERE name = ?', ('users',))
connection.commit()

# INSERT the original data into the database.
insert_query = """
INSERT INTO users (first_name, last_name, age, street, city, state, zipcode, phone, username, password)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""
users_list = [
    ('Alice', 'Johnson', 28, '123 Maple St', 'Rivertown', 'CA', '90210', '555-1234', 'alicej', 'passA1'),
    ('Brian', 'Smith', 34, '456 Oak Ave', 'Greenville', 'NY', '12083', '555-2345', 'bsmith', 'passB2'),
    ('Chloe', 'Martinez', 22, '789 Pine Rd', 'Lakeside', 'FL', '32750', '555-3456', 'chloem', 'passC3'),
    ('David', 'Nguyen', 45, '135 Elm St', 'Springfield', 'IL', '62704', '555-4567', 'dnguyen', 'passD4'),
    ('Ella', 'Brown', 31, '246 Cedar Ln', 'Fairview', 'TX', '75069', '555-5678', 'ellab', 'passE5'),
    ('Frank', 'Wilson', 38, '357 Birch Blvd', 'Oakville', 'OR', '97045', '555-6789', 'fwilson', 'passF6'),
    ('Grace', 'Lee', 29, '468 Redwood St', 'Harborview', 'WA', '98101', '555-7890', 'glee', 'passG7'),
    ('Henry', 'Adams', 52, '579 Spruce Dr', 'Mountainview', 'CO', '80301', '555-8901', 'hadams', 'passH8'),
    ('Isla', 'Thomas', 24, '680 Ash Ct', 'Brookfield', 'WI', '53005', '555-9012', 'ithomas', 'passI9'),
    ('Jack', 'Garcia', 36, '791 Beech Way', 'Riverbend', 'GA', '30303', '555-0123', 'jgarcia', 'passJ0'),
    ('Kara', 'Robinson', 27, '852 Willow Pl', 'Newhaven', 'MA', '02130', '555-1122', 'krobinson', 'kpass1'),
    ('Liam', 'Clark', 33, '963 Cypress Ave', 'Kingsport', 'TN', '37660', '555-2233', 'lclark', 'lpass2'),
    ('Mia', 'Walker', 41, '107 Fir St', 'Ashville', 'NC', '28801', '555-3344', 'mwalker', 'mpass3'),
    ('Noah', 'Hall', 26, '118 Hickory Ln', 'Plainfield', 'IN', '46168', '555-4455', 'nhall', 'npass4'),
    ('Olivia', 'Allen', 39, '129 Larch Rd', 'Mapleton', 'UT', '84664', '555-5566', 'oallen', 'opass5'),
    ('Peter', 'Young', 48, '140 Hemlock Dr', 'Rockport', 'ME', '04856', '555-6677', 'pyoung', 'ppass6'),
    ('Quinn', 'Wright', 30, '151 Aspen Ln', 'Silverlake', 'NV', '89433', '555-7788', 'qwright', 'qpass7'),
    ('Rachel', 'King', 35, '162 Cottonwood St', 'Bayville', 'NJ', '08721', '555-8899', 'rking', 'rpass8'),
    ('Sam', 'Lopez', 40, '173 Magnolia Ave', 'Portland', 'ME', '04101', '555-9900', 'slopez', 'spass9'),
    ('Tina', 'Harris', 37, '184 Dogwood Blvd', 'Oceanview', 'SC', '29577', '555-1010', 'tharris', 'tpass0'),
    ('Umar', 'Mitchell', 42, '195 Alder Ct', 'Sunset', 'AZ', '85001', '555-2020', 'umitchell', 'upass1'),
    ('Vera', 'Bailey', 32, '206 Sequoia Dr', 'Lakewood', 'WA', '98499', '555-3030', 'vbailey', 'vpass2'),
    ('Wes', 'Scott', 46, '217 Sycamore Way', 'Elmhurst', 'IL', '60126', '555-4040', 'wscott', 'wpass3'),
    ('Xena', 'Carter', 23, '228 Tamarack St', 'Greenfield', 'MA', '01301', '555-5050', 'xcarter', 'xpass4'),
    ('Yuri', 'Patterson', 44, '239 Poplar Ave', 'Harmony', 'PA', '16037', '555-6060', 'ypatterson', 'ypass5'),
    ('Zoe', 'Price', 29, '250 Juniper Rd', 'Harmony', 'VT', '05001', '555-7070', 'zprice', 'zpass6')
]

cursor.executemany(insert_query, users_list)
connection.commit()
connection.close()
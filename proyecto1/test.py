import requests

data = {'key': 'value'}
response = requests.post('http://127.0.0.1:5000/', json=data)

print('Status Code:', response.status_code)
print('Response Body:', response.text)


import sqlite3

def get_all_tables(conn):
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [table[0] for table in c.fetchall()]

def get_columns(conn, table_name):
    c = conn.cursor()
    c.execute(f"PRAGMA table_info({table_name})")
    return [column[1] for column in c.fetchall()]

# Create a connection to the database
conn = sqlite3.connect('employee.db')  # Replace 'employee.db' with the name of your database

# Get columns of all tables
tables = get_all_tables(conn)
for table in tables:
    columns = get_columns(conn, table)
    print(f"Table {table}: {columns}")

# Close the connection to the database
conn.close()
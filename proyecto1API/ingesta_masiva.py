import sqlite3
# ingesta masiva 
def insert_batch_transactions(conn, table_name, transactions):
    c = conn.cursor()

    # Assuming each transaction is a tuple of values
    placeholders = ', '.join('?' for _ in transactions[0])
    query = f"INSERT INTO {table_name} VALUES ({placeholders})"

    c.executemany(query, transactions)
    conn.commit()

# Create a connection to the database
conn = sqlite3.connect('employee.db') 

# Insert batch transactions
# Replace 'table_name' with the name of your table
# Replace 'transactions' with your list of transactions
insert_batch_transactions(conn, 'table_name', transactions)

conn.close()    
#brings back name of tables and columns 
# 
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('employee.db')

# Create a cursor
c = conn.cursor()

# tables and columns 

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = c.fetchall()

for table in tables:
    table_name = table[0]
    c.execute(f"PRAGMA table_info({table_name});")
    columns = c.fetchall()
    print(f"Table: {table_name}")
    for column in columns:
        print(f"Column: {column[1]}")
        
        
conn.close()
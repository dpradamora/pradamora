import csv
import sqlite3

def insert_csv_data_into_db(conn, table_name, csv_file_path):
    c = conn.cursor()

    # Read the CSV file
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        columns = next(reader)  # Assumes the first row in your CSV contains column names
        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join('?' for _ in columns)})"

        for row in reader:
            c.execute(query, row)

    conn.commit()

# Create a connection to the database
conn = sqlite3.connect('employee.db') 

# Insert CSV data into the database
# Replace 'table_name' with the name of your table
# Replace 'path_to_your_file.csv' with the path to your CSV file
insert_csv_data_into_db(conn, 'table_name', 'path_to_your_file.csv')

conn.close()
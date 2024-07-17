import sqlite3
import csv

def add_data_from_csv(conn, table_name, csv_file):
    c = conn.cursor()

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        columns = next(reader) 
        columns_str = "\", \"".join(columns)
        query = f'INSERT INTO {table_name} ("{columns_str}") VALUES ({", ".join("?" for _ in columns)})'

        for row in reader:
            c.execute(query, row)

    conn.commit()

# Crear una conexión a la base de datos
conn = sqlite3.connect('employee.db')  # Reemplaza 'employee.db' con el nombre de tu base de datos

# Añadir datos a las tablas desde archivos CSV
add_data_from_csv(conn, 'hired_employees', '/Users/daniel.prada/Downloads/hired_employees.csv')
add_data_from_csv(conn, 'departments', '/Users/daniel.prada/Downloads/departments.csv')
add_data_from_csv(conn, 'jobs', '/Users/daniel.prada/Downloads/jobs.csv')

# Cerrar la conexión a la base de datos
conn.close()
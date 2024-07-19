#brings back name of tables and columns so we can use them in the API

import sqlite3

def list_tables():
    conn = sqlite3.connect('employee.db')  # Asegúrate de que 'employee.db' es el nombre de tu base de datos
    c = conn.cursor()

    # Consulta para listar todas las tablas en la base de datos
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")

    print(c.fetchall())

    conn.close()

# Llama a la función para listar las tablas
list_tables()



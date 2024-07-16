import sqlite3
import pandas as pd


def create_connection():
    conn = sqlite3.connect('employee')
    print(conn)
    return conn

def create_table(conn):
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT UNIQUE
        )
    ''')
    conn.commit()

def add_user(conn, name, email):
    c = conn.cursor()
    c.execute('INSERT INTO users(name, email) VALUES(?, ?)', (name, email))
    conn.commit()

def close_connection(conn):
    conn.close()


def populate_table_from_csv(conn, table_name, csv_file_path):
    df = pd.read_csv(csv_file_path)
    df.to_sql(table_name, conn, if_exists='append', index=False)
    
""" conn = database.create_connection()
database.populate_table_from_csv(conn, 'table1', 'table1.csv')
database.populate_table_from_csv(conn, 'table2', 'table2.csv')
database.populate_table_from_csv(conn, 'table3', 'table3.csv')
database.close_connection(conn)"""



def create_tables():
    conn = sqlite3.connect('employee')  # Reemplaza 'my_database.db' con el nombre de tu base de datos
    c = conn.cursor()

    # Crear la tabla hired_employees
    c.execute('''
        CREATE TABLE IF NOT EXISTS hired_employees (
            id INTEGER,
            name TEXT,
            datetime TEXT,
            department_id INTEGER,
            job_id INTEGER
        )
    ''')

    # Crear la tabla departments
    c.execute('''
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER,
            department TEXT
        )
    ''')

    # Crear la tabla jobs
    c.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER,
            job TEXT
        )
    ''')
    
def list_tables():
    conn = sqlite3.connect('employee.db')  # Reemplaza 'my_database.db' con el nombre de tu base de datos
    c = conn.cursor()

    # Consulta para listar todas las tablas en la base de datos
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")

    print(c.fetchall())

    conn.close()

# Llama a la función para listar las tablas
list_tables()

from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/hired_employees')
def hired_employees():
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()

    c.execute("SELECT * FROM hired_employees;")
    employees = c.fetchall()

    conn.close()

    return jsonify(employees)

@app.route('/departments')
def departments():
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()

    c.execute("SELECT * FROM departments;")
    departments = c.fetchall()

    conn.close()

    return jsonify(departments)

@app.route('/jobs')
def jobs():
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()

    c.execute("SELECT * FROM jobs;")
    jobs = c.fetchall()

    conn.close()

    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)
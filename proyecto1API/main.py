import sqlite3
import pandas as pd
from flask import Flask, jsonify
import pandas as pd
import csv


def create_connection():
    conn = sqlite3.connect('employee.db')
    print(conn)
    return conn


def add_user(conn, name, email):
    c = conn.cursor()
    c.execute('INSERT INTO users(name, email) VALUES(?, ?)', (name, email))
    conn.commit()


def close_connection(conn):
    conn.close()


def populate_table_from_csv(conn, table_name, csv_file_path):
    df = pd.read_csv(csv_file_path)
    df.to_sql(table_name, conn, if_exists='append', index=False)
    
    
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

def create_tables():
    conn = sqlite3.connect('employee.db')  
    c = conn.cursor()
#creacion de las tres tablas del proyecto

    #  hired_employees
    c.execute('''
        CREATE TABLE IF NOT EXISTS hired_employees (
            id INTEGER,
            name TEXT,
            datetime TEXT,
            department_id INTEGER,
            job_id INTEGER
        )
    ''')

    #  departments
    c.execute('''
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER,
            department TEXT
        )
    ''')

    #  jobs
    c.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER,
            job TEXT
        )
    ''')
    
def list_tables():
    conn = sqlite3.connect('employee.db')  
    c = conn.cursor()

   
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")

    print(c.fetchall())

    conn.close()

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

@app.route('/tables')
def tables():
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()

    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()

    conn.close()

    tables = [table[0] for table in tables]

    return jsonify(tables)

create_tables()

#csv files
conn = sqlite3.connect('employee.db')
add_data_from_csv(conn, 'hired_employees', '/Users/daniel.prada/Downloads/hired_employees.csv')
add_data_from_csv(conn, 'departments', '/Users/daniel.prada/Downloads/departments.csv')
add_data_from_csv(conn, 'jobs', '/Users/daniel.prada/Downloads/jobs.csv')


if __name__ == '__main__':
    app.run(debug=True, port=4500)
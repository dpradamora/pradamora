
import sqlite3
import pandas as pd
from flask import Flask, jsonify
import pandas as pd
import csv
from main import create_connection, add_user, close_connection, populate_table_from_csv, add_data_from_csv, create_tables
from flask import Flask, request, jsonify


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
@app.route('/')
def home():
    return "<h1>Welcome to the API! Available endpoints:</br> <a href='/hired_employees'>hired_employees</a> </br> <a href='/departments'>departments</a> </br> <a href='/jobs'>jobs</a></h1>"

if __name__ == '__main__':
        create_tables()  # Create the tables if they don't exist
        app.run(debug=True, port=4500)

@app.route('/tables')
def tables():
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()

        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()

        conn.close()

        tables = [table[0] for table in tables]

        return jsonify(tables)

if __name__ == '__main__':
    app.run(debug=True, port=4500)
    
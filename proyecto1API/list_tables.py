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



def create_tables():
    conn = sqlite3.connect('employee.db')  # Reemplaza 'employee.db' con el nombre de tu base de datos
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

    conn.commit()
    conn.close()

create_tables()
list_tables()

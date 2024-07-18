import sqlite3

# Create a connection to the database
conn = sqlite3.connect('employee.db')

# Create a cursor
c = conn.cursor()

# Get the names of all tables in the database
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = c.fetchall()
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = c.fetchall()
print(tables)
# Print the tables
for table in tables:
    print(f"Table: {table[0]}")


query = """
SELECT d.department, j.job, 
       SUM(CASE WHEN strftime('%m', e.datetime) BETWEEN '01' AND '03' THEN 1 ELSE 0 END) AS Q1,
       SUM(CASE WHEN strftime('%m', e.datetime) BETWEEN '04' AND '06' THEN 1 ELSE 0 END) AS Q2,
       SUM(CASE WHEN strftime('%m', e.datetime) BETWEEN '07' AND '09' THEN 1 ELSE 0 END) AS Q3,
       SUM(CASE WHEN strftime('%m', e.datetime) BETWEEN '10' AND '12' THEN 1 ELSE 0 END) AS Q4
FROM hired_employees e
JOIN departments d ON e.department_id = d.id
JOIN jobs j ON e.job_id = j.id
WHERE strftime('%Y', e.datetime) = '2021'
GROUP BY  d.department, j.job
"""

# Execute the query
c.execute(query)

# Fetch all the results
results = c.fetchall()

# Print the results
for row in results:
    print(f"Department ID: {row[0]}, Job ID: {row[1]}, Q1: {row[2]}, Q2: {row[3]}, Q3: {row[4]}, Q4: {row[5]}")

# Close the connection to the database
conn.close()

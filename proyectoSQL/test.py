import sqlite3

# Create a connection to the database
conn = sqlite3.connect('employee.db')

# Create a cursor
c = conn.cursor()


# calculate average # of
c.execute("""
SELECT AVG(hired_count)
FROM (
    SELECT COUNT(*) as hired_count
    FROM hired_employees
    WHERE strftime('%Y', datetime) = '2021'
    GROUP BY department_id
)
""")
mean_hired = c.fetchone()[0]

# Define your SQL query
query # Replace 'your_table' with the name of your table
c.execute("PRAGMA table_info(your_table)")
columns = c.fetchall()

for column in columns:
    print(column)
c = f"""
SELECT d.id, d.department, COUNT(*) as num_hired
FROM hired_employees e
JOIN departments d ON e.department_id = d.id
WHERE strftime('%Y', e.datetime) = '2021'
GROUP BY dept.id, d.department
HAVING num_hired > {mean_hired}
ORDER BY num_hired DESC
"""

# Execute the query
c.execute(query)

# Fetch all the results
results = c.fetchall()

# Print the results
for row in results:
    print(f" {row[0]},  {row[1]}, {row[2]}")

# Close the connection to the database
conn.close()
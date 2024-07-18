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
query = f"""
SELECT dept.id, dept.department, COUNT(*) as num_hired
FROM hired_employees emp
JOIN departments dept ON emp.department_id = dept.id
WHERE strftime('%Y', emp.datetime) = '2021'
GROUP BY dept.id, dept.department
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
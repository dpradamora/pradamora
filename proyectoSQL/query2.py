import sqlite3
import csv 

# Create a connection to the database
conn = sqlite3.connect('employee.db')

# Create a cursor
c = conn.cursor()

#tables = ("hired_employees", "departments", "jobs")
#columns = []
#for table in tables:
#    c.execute(f"PRAGMA table_info({table});")
#    columns.extend(c.fetchall())


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
    
query = f"""
SELECT d.id, d.department, COUNT(*) as num_hired
FROM hired_employees e
JOIN departments d ON e.department_id = d.id
WHERE strftime('%Y', e.datetime) = '2021'
GROUP BY d.id, d.department
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


# Save he results to a CSV file
filename = '/Users/daniel.prada/pradamora/proyectoSQL/results2.csv'
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['department', 'job', 'q1'])
    writer.writerows(results)

print(f"CSV file '{filename}' created successfully.")

# Fetch all the results
c.execute(query)
results = c.fetchall()

# Define the "columns" variable
#columns = [column[1] for column in c.description]

#for column in columns:
#    print(column)
    

# Close the connection to the database
conn.close()
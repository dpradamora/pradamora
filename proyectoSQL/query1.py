import sqlite3
import sys
import csv


# Create a connection to the database
conn = sqlite3.connect('employee.db')
# Create a cursor object
cursor = conn.cursor()

# Check if the hired_employees table is empty

cursor.execute("SELECT COUNT(*) FROM hired_employees")
count = cursor.fetchone()[0]

query =  f"""
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
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Print the results
try:
    for row in results:
        print(f"Department: {row[0]}, Job: {row[1]}, Q1: {row[2]}, Q2: {row[3]}, Q3: {row[4]}, Q4: {row[5]}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Save the results to a CSV file
filename = '/Users/daniel.prada/pradamora/proyectoSQL/results1.csv'
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Department', 'Job', 'Q1', 'Q2', 'Q3', 'Q4'])
    writer.writerows(results)

print(f"CSV file '{filename}' created successfully.")
# Fetch all the results
results = cursor.fetchall()
# Print the results

try:
        for row in results:
            print(f"Department ID: {row[0]}, Job ID: {row[1]}, Q1: {row[2]}, Q2: {row[3]}, Q3: {row[4]}, Q4: {row[5]}")
        
except Exception as e:
            print(f"An error occurred: {str(e)}")


            # Close the cursor
conn.close()

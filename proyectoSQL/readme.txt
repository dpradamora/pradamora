Section 2: SQL
You need to explore the data that was inserted in the previous section. The stakeholders ask
for some specific metrics they need. You should create an end-point for each requirement.
Requirements
● Number of employees hired for each job and department in 2021 divided by quarter. The
table must be ordered alphabetically by department and job.
Output example:
department job Q1 Q2 Q3 Q4
Staff Recruiter 3 0 7 11
Staff Manager 2 1 0 2
Supply Chain Manager 0 1 3 0

● List of ids, name and number of employees hired of each department that hired more
employees than the mean of employees hired in 2021 for all the departments, ordered
by the number of employees hired (descending).
Output example:
id department hired
7 Staff 45
9 Supply Chain 12

SELECT department, job, 
       SUM(CASE WHEN strftime('%m', hire_date) BETWEEN '01' AND '03' THEN 1 ELSE 0 END) AS Q1,
       SUM(CASE WHEN strftime('%m', hire_date) BETWEEN '04' AND '06' THEN 1 ELSE 0 END) AS Q2,
       SUM(CASE WHEN strftime('%m', hire_date) BETWEEN '07' AND '09' THEN 1 ELSE 0 END) AS Q3,
       SUM(CASE WHEN strftime('%m', hire_date) BETWEEN '10' AND '12' THEN 1 ELSE 0 END) AS Q4
FROM employees
WHERE strftime('%Y', hire_date) = '2021'
GROUP BY department, job
ORDER BY department, job;
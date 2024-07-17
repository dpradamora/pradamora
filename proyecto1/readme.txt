hired_employees.csv:
id INTEGER Id of the employee
name STRING Name and surname of the employee
datetime STRING Hire datetime in ISO format
department_id INTEGER Id of the department which the employee was hired for
job_id INTEGER Id of the job which the employee was hired for


File hired_employees.csv  
departments.csv
id INTEGER Id of the department
department STRING Name of the department

1, Supply Chain
2, Maintenance
3, Staff
File departments.csv should be attached by recruiter
jobs.csv:
id INTEGER Id of the job
job STRING Name of the job

1, Recruiter
2, Manager
3, Analyst
File jobs.csv should be attached by recruiter


-- Crear la tabla hired_employees
CREATE TABLE hired_employees (
    id INTEGER,
    name STRING,
    datetime STRING,
    department_id INTEGER,
    job_id INTEGER
);

-- Crear la tabla departments
CREATE TABLE departments (
    id INTEGER,
    department STRING
);

-- Crear la tabla jobs
CREATE TABLE jobs (
    id INTEGER,
    job STRING
);
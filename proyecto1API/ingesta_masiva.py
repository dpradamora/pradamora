
from faker import Faker
import random
from datetime import datetime, timedelta
import random
from faker import Faker
import csv

def create_random_csv(file_name, num_records):
    # Create a Faker instance
    fake = Faker()
    
    # Define the column names
    column_names = ['name', 'datetime', 'department_id', 'job_id']

    # Open the CSV file in write mode
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)

        # Write the column names
        writer.writerow(column_names)

        # Write num_records random records
        for _ in range(num_records):
            # Generate random data
            name = fake.name()
            datetime = fake.date_time_this_century()
            department_id = random.randint(1, 10)
            job_id = random.randint(1, 10)

            # Write the data
            writer.writerow([name, datetime, department_id, job_id])
def create_random_csv(file_name, num_records):
    # Create a Faker instance
    fake = Faker()
    
    # Define the column names
    column_names = ['name', 'datetime', 'department_id', 'job_id']

    # Open the CSV file in write mode
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)

        # Write the column names
        writer.writerow(column_names)

        # Write num_records random records
        for _ in range(num_records):
            # Generate random data
            name = fake.first_name()
            datetime = fake.date_time_this_century()
            department_id = random.randint(1, 10)
            job_id = random.randint(1, 10)

            # Write the data
            writer.writerow([name, datetime, department_id, job_id])

# Create a CSV file with 1000 random records
# Replace 'hired_employee.csv' with your desired file name
create_random_csv('hired_employee.csv', 1000)

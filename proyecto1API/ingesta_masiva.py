
from faker import Faker
import random
from datetime import datetime, timedelta
import random
from faker import Faker
import csv
import csv
from faker import Faker
import random
# Define the file name and number of records
file_name = 'hired_employee.csv'
num_records = 1000

# Create a Faker instance
fake = Faker()

# Define the column names
column_names = ['name', 'datetime', 'department_id', 'job_id']

# Open the CSV file in write mode

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
            datetime = fake.date_time()
            department_id = random.randint(1, 10)
            job_id = random.randint(1, 10)

            # Write the data
            writer.writerow([name, datetime, department_id, job_id])

# Create random  
create_random_csv('/Users/daniel.prada/pradamora/proyectoSQL/prueba1.csv', 1000)

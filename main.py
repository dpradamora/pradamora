import requests

import csv

# Function to upload CSV data to the API endpoint
def upload_csv_data(file_path, endpoint):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    
    # Make a POST request to the API endpoint with the CSV data
    response = requests.post(endpoint, json=data)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print('CSV data uploaded successfully')
    else:
        print('Failed to upload CSV data:', response.text)

# Function to insert batch transactions to the API endpoint
def insert_batch_transactions(transactions, endpoint):
    # Make a POST request to the API endpoint with the batch transactions
    response = requests.post(endpoint, json=transactions)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print('Batch transactions inserted successfully')
    else:
        print('Failed to insert batch transactions:', response.text)

# Example usage
csv_file_path = '/Users/daniel.prada/Downloads/file.csv'
api_endpoint = 'http://127.0.0.1:5000/'

# Upload historical data from CSV file
upload_csv_data(csv_file_path, api_endpoint)

# Insert batch transactions
batch_transactions = [
    {'column1': 'value1', 'column2': 'value2'},
    {'column1': 'value3', 'column2': 'value4'},
    # Add more transactions as needed
]
insert_batch_transactions(batch_transactions, api_endpoint)



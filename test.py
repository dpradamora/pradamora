import requests

data = {'key': 'value'}
response = requests.post('http://127.0.0.1:5000/', json=data)

print('Status Code:', response.status_code)
print('Response Body:', response.text)



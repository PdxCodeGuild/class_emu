import requests
response = requests.get('http://192.168.1.210:8000/my_steps.csv')
print(response.text)

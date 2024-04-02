import requests



print('testing')
response=requests.get('http://127.0.0.1:8000/market')
print(response.json())
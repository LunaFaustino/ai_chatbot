import requests

response = requests.post(
    "http://127.0.0.1:5000/api"
    json= {"ola" : "mundo", "data" : [[0,1,2]]}
)

print(response.status_code)
print(response.json)
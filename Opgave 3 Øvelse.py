import requests

url = "https://httpbin.org/get"

params = {
    "navn": "Ronni",
    "alder": 20
}

response = requests.get(url, params=params)

print("Serveren modtog:")
print(response.text)

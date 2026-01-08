import requests

url = "https://httpbin.org/get"

response = requests.get(url)

print("Status code:")
print(response.status_code)

print("\nHeaders:")
for key, value in response.headers.items():
    print(f"{key}: {value}")

print("\nResponse body:")
print(response.text)

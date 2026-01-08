import requests

url = "https://httpbin.org/headers"
response = requests.get(url)

print("=== response.headers ===")
print(response.headers)

print("\n=== response.text ===")
print(response.text)

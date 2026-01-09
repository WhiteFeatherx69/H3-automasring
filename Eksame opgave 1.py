import requests

IP = "20.91.198.208"
PORT = 8081
TOKEN = "df2e6ced"

url = f"http://{IP}:{PORT}"

response = requests.get(
    url,
    params={"token": TOKEN}
)

print("=== RESPONSE HEADERS ===")
print(response.headers)

print("\n=== RESPONSE BODY ===")
print(response.text)

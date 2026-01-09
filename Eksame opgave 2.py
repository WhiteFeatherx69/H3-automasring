import requests
from cryptography.fernet import Fernet

IP = "20.91.198.208"
PORT = 8081
TOKEN = "df2e6ced"

url = f"http://{IP}:{PORT}"

r = requests.get(url, params={"token": TOKEN})

print("=== RESPONSE HEADERS ===")
print(r.headers)

ciphertext = r.text.strip()
key = r.headers["X-Secret-Key"].encode()

f = Fernet(key)
plaintext = f.decrypt(ciphertext.encode())

print("\n=== DECRYPTED BODY ===")
print(plaintext.decode())

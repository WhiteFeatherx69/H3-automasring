import requests

MODEL = "llama3.2:latest"

print("DK→EN (lokal LLM via Ollama). Skriv /exit for at stoppe.\n")

while True:
    dk = input("DK> ").strip()
    if not dk:
        continue
    if dk.lower() == "/exit":
        break

    r = requests.post(
        "http://127.0.0.1:11434/api/chat",
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": "Translate Danish to natural English. Output ONLY the English translation."},
                {"role": "user", "content": dk},
            ],
            "stream": False,
        },
        timeout=120,
    )

    if r.status_code != 200:
        print("HTTP", r.status_code)
        print(r.text)
        continue

    data = r.json()
    print("EN>", data["message"]["content"].strip(), "\n")

from openai import OpenAI
from config import API_KEY, BASE_URL, MODEL
from prompt import SYSTEM_PROMPT
import os

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

topic = input("Masukkan topik YouTube: ")

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": f"Buat naskah YouTube 5 menit tentang: {topic}"
        }
    ]
)

script = response.choices[0].message.content

os.makedirs("output", exist_ok=True)

with open("output/script.txt", "w", encoding="utf-8") as f:
    f.write(script)

print("\n===== NASKAH =====\n")
print(script)

print("\n✅ Naskah berhasil disimpan di output/script.txt")

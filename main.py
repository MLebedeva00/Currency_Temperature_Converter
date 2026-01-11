import os
import requests
from dotenv import load_dotenv

# загружаем переменные из .env
load_dotenv()

# читаем API-ключ
API_KEY = os.getenv("API_KEY")

# проверяем, есть ли ключ
if not API_KEY:
    print("Ошибка: API-ключ не найден. Проверьте файл .env")
else:
    print("API-ключ загружен успешно!")

# текстовый запрос
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
response = requests.get(url)

if response.status_code == 200:
    print("API-ключ работает!")
    data = response.json()  # ответ на наш запрос в формате данных json (похоже на словарь)
    print(f"Пример курса: 1 USD = {data['conversion_rates']['EUR']} EUR")

# conversion_rates -- словарь валют

else:
    print(f"Ошибка: API не отвечает. Код состояния {response.status_code}")
    print(f"Сообщение от сервера: {response.text}")

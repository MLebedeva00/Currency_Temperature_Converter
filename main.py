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
    exit()
else:
    print("API-ключ загружен успешно!")

# Запрашиваем у пользователя данные для конвертации
base_currency = input("Введите код исходной валюты: ").upper()
target_currency = input("Введите код целевой валюты: ").upper()
amount = float(input("Введите сумму для конвертации: "))

# Формируем url для запроса
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"

#Делаем запрос к API
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # ответ на наш запрос в формате данных json (похоже на словарь)

    # Проверяем, успешен ли ответ
    if data['result'] == 'success':
        print("API-ключ работает!")

        # Проверяем, есть ли нужная валюта в списке
        if target_currency in data['conversion_rates']:
            rate = data['conversion_rates'][target_currency]
            converted_amount = amount * rate
            print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        else:
            print("Ошибка. Валюта не найдена в базе API")

    else:
        print("Ошибка: API не смог обработать запрос. Проверьте код валюты")

else:
    print(f"Ошибка: API не отвечает. Код состояния {response.status_code}")
    print(f"Сообщение от сервера: {response.text}")
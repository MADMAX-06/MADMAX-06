import requests
import json
import random

# Генерация случайного числа
random_number = random.randint(1, 1000)  # Генерируем целое число от 1 до 999
random_number2 = random.randint(1, 1000)  # Генерируем целое число от 1 до 999

first_names = [
    "Иван", "Алексей", "Анна", "Елена", "Михаил",
    "Ольга", "Сергей", "Татьяна", "Дмитрий", "Марина"
]

def get_random_first_name():
    return random.choice(first_names)

url = "https://petstore.swagger.io/v2/pet"

data = {
    "id": f"{random_number}",  # Получаем рандомный id
    "category": {
        "id": f"{random_number2}",  # Получаем 2й рандомный id
        "name": "dog"
    },
    "name": f"{get_random_first_name()}",  # Получаем рандомное имя
    "status": "available"
}

def test_post_pet():
    # Отправляем POST-запрос
    response = requests.post(url, json=data)

    # Проверяем статус-код ответа
    assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"

    # Проверяем содержимое ответа
    response_data = response.json()
    assert response_data["status"] == "available", "Ожидаемый статус 'available' не получен"
    assert response_data["id"] == int(f"{random_number}"), f"Ожидаемый id {random_number} не получен"

    # Форматируем JSON и выводим его
    formatted_json = json.dumps(response_data, indent=4, ensure_ascii=False)
    print("Тест пройден")
    print(f"Получены данные в формате JSON: {formatted_json}")

if __name__ == "__main__":
    test_post_pet()
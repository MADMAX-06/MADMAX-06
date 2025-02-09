import requests
import json
# Базовый URL API
BASE_URL = "https://hr.recruit.liis.su/qa0/v1/api"
# Email пользователя
email = "test@test.ru"

def test_get_users():
    # Формируем полный URL с параметрами
    url = f"{BASE_URL}/{email}/posts"

    # Выполняем GET-запрос
    response = requests.get(url)

    # Проверяем статус-код ответа
    assert response.status_code == 200

    data = response.json()

    # Форматируем JSON и выводим его
    formatted_json = json.dumps(data, indent=4, ensure_ascii=False)
    print("Тест пройден")
    print(f"Получены данные в формате JSON: {formatted_json}")

# Вызов функции
test_get_users()
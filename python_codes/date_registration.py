from datetime import datetime
import pytz

# Создаем объект временной зоны Москвы
moscow_tz = pytz.timezone('Europe/Moscow')

# Устанавливаем дату и время окончания регистрации в MSK
registration_deadline = moscow_tz.localize(datetime(2025, 2, 19, 14, 0))

# Создаем объект временной зоны
second_time = ('Europe/Samara') # Можно заменить для других проверок

# Создаем объект временной зоны second_time
city_2 = pytz.timezone(second_time)

# Устанавливаем текущее время в Samara
current_time_samara = city_2.localize(datetime(2025, 2, 19, 14, 0))

# Переводим текущее время Samara в московское время
current_time_in_moskow = current_time_samara.astimezone(moscow_tz)

# Сравниваем даты
if current_time_in_moskow <= registration_deadline:
    print("Регистрация еще открыта.")
else:
    print("Срок регистрации истек.")
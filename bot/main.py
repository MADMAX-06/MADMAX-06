import telebot # импортируем telebot
from secrets import secrets # словарь с токеном из файла secrets.py
from telebot import types # для определения типов
import random # для выбора случайного комплимента
from info_base import sql_info, structura, testirov, info_base


# передаём значение переменной с кодом экземпляру бота
token = secrets.get('BOT_API_TOKEN')
bot = telebot.TeleBot(token)


# хендлер и функция для обработки команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    # создаём кнопки бота
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = types.KeyboardButton("🚀 Старт")
    action_button = types.KeyboardButton("POST запросы")
    action_button_2 = types.KeyboardButton("Команды SQL")
    action_button_3 = types.KeyboardButton("Тестировщик")
    markup.add(start_button, action_button)
    markup.add(action_button_2)
    markup.add(action_button_3)
    # приветсвенное сообщение для команды /start
    bot.send_message(message.chat.id, text="Привет, {0.first_name} 👋\nВоспользуйся кнопками".format(message.from_user), reply_markup=markup)
    bot.send_photo(message.chat.id, photo=open('/img/bot.jpg', 'rb'))

# хендлер для обработки нажатий кнопок
@bot.message_handler(content_types=['text'])
def buttons(message):
    if (message.text == "🚀 Старт"):
        bot.send_message(message.chat.id, text="Бот содержит информацию по SQL и что такое тестирование")
    elif (message.text == "Тестировщик"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        testir_button = types.KeyboardButton("Тестирование - это")
        testir_button2 = types.KeyboardButton("Виды тестирования")
        markup.add(testir_button)
        markup.add(testir_button2)
        bot.send_message(message.chat.id, "Выберите команду:", reply_markup=markup)

    elif (message.text == "Тестирование - это"):
        bot.send_message(message.chat.id, text=testirov())

    elif (message.text == "Пример SELECT"):
        bot.send_message(message.chat.id, text=f"{random.choice(info_base)}")

    elif (message.text == "Команды SQL"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        sql_button = types.KeyboardButton("SQL-это")
        sql_select_btn = types.KeyboardButton("Структура")
        sql_select_btn2 = types.KeyboardButton("Пример SELECT")
        markup.add(sql_button)
        markup.add(sql_select_btn)
        markup.add(sql_select_btn2)

        bot.send_message(message.chat.id, "Выберите команду:", reply_markup=markup)
    elif (message.text == "SQL-это"):
        bot.send_message(message.chat.id, text=sql_info())
    elif (message.text == "Структура"):
        bot.send_message(message.chat.id, text=structura())

    else:
        bot.send_message(message.chat.id, text="Я могу отвечать только на нажатие кнопок")



# бесконечное выполнение кода
bot.polling(none_stop=True, interval=0)
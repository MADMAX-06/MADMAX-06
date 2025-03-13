import telebot
from telebot import types
from secrets import secrets

token = secrets.get('BOT_API_TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = types.KeyboardButton("🚀 Старт")

    resume_button = types.KeyboardButton("Резюме")
    markup.add(start_button)
    markup.add(resume_button)
    # приветсвенное сообщение для команды /start
    bot.send_message(message.chat.id, text="Привет, {0.first_name} 👋\nЯ бот секретарь. Я могу предоставить информацию о владельце. \nДля этого воспользуйся кнопками".format(message.from_user), reply_markup=markup)
    bot.send_photo(message.chat.id, photo=open('img/bot_info.jpg', 'rb'))


@bot.message_handler(content_types=['text'])
def button(message):
    if message.text == "🚀 Старт":
        bot.send_message(message.chat.id, text="Бот секретарь")

    elif message.text == "Резюме":
        bot.send_message(message.chat.id, text="Предоставляю резюме Рябова Максима Николаевича")
        bot.send_document(message.chat.id, document="document/Рябов Максим Николаевич.pdf")

    else:
        bot.send_message(message.chat.id, text="Я могу отвечать только на нажатие кнопок")

bot.polling(none_stop=True, interval=0)



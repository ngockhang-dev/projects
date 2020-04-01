import telebot
from telebot import types
import COVID19Py

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('889270203:AAGv8pY2c_x-h9jvTN8FpTZTlny5SVRGbQc')


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f'Привет {message.from_user.first_name}'
    bot.send_message(message.chat.id, send_mess)


# Функция, что сработает при отправке какого-либо текста боту
# Здесь мы создаем отслеживания данных и вывод статистики по определенной стране
@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
        final_message = f"Confirmed:{location[0]['latest']['confirmed']}\nDeaths:{location[0]['latest']['deaths']}"
    elif get_message_bot == "украина" or get_message_bot == "Украина":
        location = covid19.getLocationByCountryCode("UA")
        final_message = f"Confirmed:{location[0]['latest']['confirmed']}\nDeaths:{location[0]['latest']['deaths']}"
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")
        final_message = f"Confirmed:{location[0]['latest']['confirmed']}\nDeaths:{location[0]['latest']['deaths']}"
    elif get_message_bot == "беларусь":
        location = covid19.getLocationByCountryCode("BY")
        final_message = f"Confirmed:{location[0]['latest']['confirmed']}\nDeaths:{location[0]['latest']['deaths']}"
    elif get_message_bot == "вьетнам":
        location = covid19.getLocationByCountryCode("VN")
        final_message = f"Confirmed:{location[0]['latest']['confirmed']}\nDeaths:{location[0]['latest']['deaths']}"
    elif get_message_bot == "италия":
        location = covid19.getLocationByCountryCode("IT")
        final_message = f"Confirmed:{location[0]['latest']['confirmed']}\nDeaths:{location[0]['latest']['deaths']}"
    elif get_message_bot == "франция":
        location = covid19.getLocationByCountryCode("FR")
        final_message = f"Confirmed:{location[0]['latest']['confirmed']}\nDeaths:{location[0]['latest']['deaths']}"
    elif get_message_bot == "германия":
        location = covid19.getLocationByCountryCode("DE")
        final_message = f"Confirmed:{location[0]['latest']['confirmed']}\nDeaths:{location[0]['latest']['deaths']}"
    elif get_message_bot == "япония":
        location = covid19.getLocationByCountryCode("JP")
        final_message = f"Confirmed:{location[0]['latest']['confirmed']}\nDeaths:{location[0]['latest']['deaths']}"
    else:
        location = covid19.getLatest()
        final_message = f"Confirmed:{location['confirmed']}\nDeaths:{location['deaths']}"

    bot.send_message(message.chat.id, final_message)


# Это нужно чтобы бот работал всё время
bot.polling(none_stop=True)

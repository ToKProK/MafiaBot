import telebot
import webbrowser

Mafia = telebot.TeleBot('6847605581:AAFshf6F811PHzdMu98gvEg26RRNOrLf2Y8')


@Mafia.message_handler(commands=['start'])
def main(message):
    Mafia.send_message(message.chat.id, 'Привет!')

@Mafia.message_handler(commands=["open_new_bot"])
def new_bot_open(message):
    webbrowser.open("https://t.me/Punching_phone_bot")

@Mafia.message_handler(func=lambda message: message.text.lower() == 'hello')
def info(message):
    Mafia.send_message(message.chat.id, 'Hello')

@Mafia.message_handler(commands=["get_my_name"])# Команда, которая демонстрирует возможность обращения к пользоваелю по имени
def info(message):
    Mafia.send_message(message.chat.id, f'Привет: {message.from_user.first_name} {message.from_user.last_name}')


@Mafia.message_handler(func=lambda message: message.text.lower() == 'id')
def idd(message):
    Mafia.send_message(message.chat.id, 'idd')


Mafia.polling(none_stop=True)

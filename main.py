import telebot

Mafia = telebot.TeleBot('6847605581:AAFshf6F811PHzdMu98gvEg26RRNOrLf2Y8')


@Mafia.message_handler(commands=['start'])
def main(message):
    Mafia.send_message(message.chat.id, 'Привет!')


@Mafia.message_handler(func=lambda message: message.text.lower() == 'hello')
def info(message):
    Mafia.send_message(message.chat.id, 'Hello')


@Mafia.message_handler(func=lambda message: message.text.lower() == 'idd')
def idd(message):
    Mafia.send_message(message.chat.id, 'idd')

Mafia.polling(none_stop=True)
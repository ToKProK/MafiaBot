import telebot
import webbrowser

Mafia = telebot.TeleBot('6847605581:AAFshf6F811PHzdMu98gvEg26RRNOrLf2Y8')


@Mafia.message_handler(commands=['start'])
def main(message):
    Mafia.send_message(message.chat.id, 'Привет я всего лишь бот, который поможет вам начать игру.При помощи команд вы сможеле:/help - узнать информацию о командах, /play - узнать правило игры, /rules - узнать правило игры!')

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
    Mafia.send_message(message.chat.id, 'Присутствуют такие команды как: /rules (Правило игры), /play (присоедениться к игре)') #команда выводит команды для использования бота

@Mafia.message_handler(func=lambda message: message.text.lower() == '/rules')
def idd(message):
    Mafia.send_message(message.chat.id, 'Правило игры!!!Мирные жители узнают что в их городе есть мафия, и они пытаються методом голосования посадить их в тюрму.Мафия же пытаются убить всех мирных жителей.У мрных жителей есть доктор и коммисар. Доктор пытается вылечит всех мирных жителей для их спасения, а коммисар пытается вычеслить мафию для помощи жителям в голосовании. Сасмое главное в этой игре коммуникация (умение лгать или же доказывать правду). Желаю вам удачи и приятной игры!!!') # команда выводит текст с правилом игры



@Mafia.message_handler()
def info(message):
    Mafia.send_message(message.chat.id, 'Я всего лишь бот, воспользуйтесь командой /help') # при написании любого текста бот выводит данный текст


Mafia.polling(none_stop=True) # не даёт выключать компиляцию

Mafia.polling(none_stop=True)

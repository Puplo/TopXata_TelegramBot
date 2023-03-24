from bs4 import BeautifulSoup
import requests
import telebot
from telebot import types
from random import *

API_TOKEN = '##############'    #bot api

bot = telebot.TeleBot(API_TOKEN)

users = [1111, 22222, 33333, 44444, -555555]    #telegram users id для небольшой защиты...


urlKek = "https://www.anekdot.ru/random/anekdot/"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36"
}


@bot.message_handler(func=lambda message: message.chat.id not in users)
def some(message):
    bot.send_message(message.chat.id, 'Ты кто такой? Иди нахуй!')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    event = types.KeyboardButton('Сходка🎉')
    members = types.KeyboardButton('Участники🧑‍🤝‍🧑')
    money = types.KeyboardButton('Реквизиты для перевода💸')
    moneydance = types.KeyboardButton('За деньги да🤑')
    anek = types.KeyboardButton('Анекдот🤣')
    rolls = types.KeyboardButton('Рулетка🎰')
    markup.add(event, members, money, anek, rolls, moneydance)
    bot.send_message(message.chat.id, '<b>Привет!, Вітаю!, Hello!,</b> שלום!', parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text(message):
    match message.text:
        case "Сходка🎉":
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Адрес", url="???????????")) #метка геолокации (пример: https://yandex.ru/maps/-/CCUSRVTyTC)
            bot.send_message(message.chat.id, f'<b>ДАТА:</b>\n <b>??????????????????', reply_markup=markup, parse_mode='html') #дата проведения мероприятия....

        case "Участники🧑‍🤝‍🧑":
            bot.send_message(message.chat.id,f'<b>СПИСОК УЧАСТНИКОВ</b>\n\n 1. ????????\n 2. ???????\n 3. ???????\n <b>4. ???????</b>\n 5. ???????\n 6. ???????\n 7. ???????\n 8. ???????',parse_mode='html') #братики

        case "Реквизиты для перевода💸":
            bot.send_message(message.chat.id, f'<b>Телефон для перевода:</b>', parse_mode='html')
            bot.send_message(message.chat.id, f'???????', parse_mode='html') #телефон
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Оплатить", url="???????")) #ссылочка на донатики(пример: киви)
            bot.send_message(message.chat.id, f'(Альфа-банк, Сбер, Tinkoff)', reply_markup=markup, parse_mode='html')

        case "За деньги да🤑":
            bot.send_message(message.chat.id, f'за деньги да🤑💵🤑', parse_mode='html')
            bot.send_animation(message.chat.id, r'https://media.giphy.com/media/7Zkj8WHtpAyk9506b3/giphy-downsized-large.gif')

        case "stop":
            bot.send_message(message.chat.id,'Ухожу...', reply_markup=types.ReplyKeyboardRemove())

        case "Анекдот🤣":
            rs = requests.get(urlKek)
            bs = BeautifulSoup(rs.text, 'html.parser')
            root = bs.find('div', class_='text')
            text = root.text
            bot.send_message(message.chat.id, text[:300], parse_mode='html')

        case "Рулетка🎰":
            roll = randint(1, 100)
            bot.send_message(message.chat.id, f"<b>{message.from_user.username}</b>, выбил <b>{roll}</b> [1-100]",parse_mode='html')


bot.polling(none_stop=True)

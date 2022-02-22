# -*- coding: utf-8 -*-
import random
from xml.sax.handler import property_interning_dict
import config
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot(config.TOKEN)
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Метод, который получает сообщения и обрабатывает их
print('ОСНОВНОЙ ЗАПУЩЕН')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «/start»
    if message.text == "/start":
        print('+1')
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        key_about = types.InlineKeyboardButton(text='Разработчик', callback_data='developer')
        keyboard.add(key_about)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Напишите вашу группу: \n\n(Например: 61 или 20-ТПИ)', reply_markup=keyboard)
    elif message.text == "58":
        bot.send_message(message.from_user.id, '@atts58_bot')
    elif message.text == "59":
        bot.send_message(message.from_user.id, '@atts59_bot')
    elif message.text == "60":
        bot.send_message(message.from_user.id, '@atts60_bot')
    elif message.text == "61":
        bot.send_message(message.from_user.id, '@atts61_bot')
    elif message.text == "62":
        bot.send_message(message.from_user.id, '@atts62_bot')
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши свою группу \n\n(Например: 61 или 20-ТПИ).")
# Обработчик нажатий на кнопки


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # 
    if call.data == "developer": 
        bot.send_message(call.message.chat.id, "ВК: vk.com/WirelessGOD \nТелеграмм: @WirelesssGOD")
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)
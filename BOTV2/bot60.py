# -*- coding: utf-8 -*-
import config
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot(config.TOKEN60)
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
import openpyxl
# Метод, который получает сообщения и обрабатывает их
print('60 ЗАПУЩЕН')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «/start»
    if message.text == "/start":
        print('+1')
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет. Я создан для того чтобы облегчить тебе жизнь (ГРУППА 60)")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого дня недели
        key_pon = types.InlineKeyboardButton(text='Понедельник', callback_data='pon')
        # И добавляем кнопку на экран
        keyboard.add(key_pon)
        key_vtr = types.InlineKeyboardButton(text='Вторник', callback_data='vtr')
        keyboard.add(key_vtr)
        key_srd = types.InlineKeyboardButton(text='Среда', callback_data='srd')
        keyboard.add(key_srd)
        key_chet = types.InlineKeyboardButton(text='Четверг', callback_data='chet')
        keyboard.add(key_chet)
        key_piat = types.InlineKeyboardButton(text='Пятница', callback_data='piat')
        keyboard.add(key_piat)
        key_subb = types.InlineKeyboardButton(text='Суббота', callback_data='subb')
        keyboard.add(key_subb)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери день недели:', reply_markup=keyboard)
    elif message.text == "Назад":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет. Я создан для того чтобы облегчить тебе жизнь (ГРУППА 60)")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого дня недели
        key_pon = types.InlineKeyboardButton(text='Понедельник', callback_data='pon')
        # И добавляем кнопку на экран
        keyboard.add(key_pon)
        key_vtr = types.InlineKeyboardButton(text='Вторник', callback_data='vtr')
        keyboard.add(key_vtr)
        key_srd = types.InlineKeyboardButton(text='Среда', callback_data='srd')
        keyboard.add(key_srd)
        key_chet = types.InlineKeyboardButton(text='Четверг', callback_data='chet')
        keyboard.add(key_chet)
        key_piat = types.InlineKeyboardButton(text='Пятница', callback_data='piat')
        keyboard.add(key_piat)
        key_subb = types.InlineKeyboardButton(text='Суббота', callback_data='subb')
        keyboard.add(key_subb)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери день недели:', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши день недели.")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # 
    if call.data == "pon": 
        # 
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на понедельник:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparP60 + ' [' + str(config.kabP601) + ']\n' + 'Вторая пара: ' + config.twoparP60 + ' [' + str(config.kabP602) + ']\n' + 'Третья пара: ' + config.threeparP60 + ' [' + str(config.kabP603) + ']\n' + 'Четвёртая пара: ' + config.fourparP60 + ' [' + str(config.kabP604) + ']\n' + 'Пятая пара: ' + config.fiveparP60 + ' [' + str(config.kabP605) + ']\n' + 'Шестая пара: ' + config.sixparP60 + ' [' + str(config.kabP606) + ']\n'
    elif call.data == "vtr":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на вторник:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparV60 + ' [' + str(config.kabV601) + ']\n' + 'Вторая пара: ' + config.twoparV60 + ' [' + str(config.kabV602) + ']\n' + 'Третья пара: ' + config.threeparV60 + ' [' + str(config.kabV603) + ']\n' + 'Четвёртая пара: ' + config.fourparV60 + ' [' + str(config.kabV604) + ']\n' + 'Пятая пара: ' + config.fiveparV60 + ' [' + str(config.kabV605) + ']\n' + 'Шестая пара: ' + config.sixparV60 + ' [' + str(config.kabV606) + ']\n'
    elif call.data == "srd":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на среду:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparS60 + ' [' + str(config.kabS601) + ']\n' + 'Вторая пара: ' + config.twoparS60 + ' [' + str(config.kabS602) + ']\n' + 'Третья пара: ' + config.threeparS60 + ' [' + str(config.kabS603) + ']\n' + 'Четвёртая пара: ' + config.fourparS60 + ' [' + str(config.kabS604) + ']\n' + 'Пятая пара: ' + config.fiveparS60 + ' [' + str(config.kabS605) + ']\n' + 'Шестая пара: ' + config.sixparS60 + ' [' + str(config.kabS606) + ']\n'
    elif call.data == "chet":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на четверг:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.onepar460 + ' [' + str(config.kab4601) + ']\n' + 'Вторая пара: ' + config.twopar460 + ' [' + str(config.kab4602) + ']\n' + 'Третья пара: ' + config.threepar460 + ' [' + str(config.kab4603) + ']\n' + 'Четвёртая пара: ' + config.fourpar460 + ' [' + str(config.kab4604) + ']\n' + 'Пятая пара: ' + config.fivepar460 + ' [' + str(config.kab4605) + ']\n' + 'Шестая пара: ' + config.sixpar460 + ' [' + str(config.kab4606) + ']\n'
    elif call.data == "piat":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на пятницу:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparPI60 + ' [' + str(config.kabPI601) + ']\n' + 'Вторая пара: ' + config.twoparPI60 + ' [' + str(config.kabPI602) + ']\n' + 'Третья пара: ' + config.threeparPI60 + ' [' + str(config.kabPI603) + ']\n' + 'Четвёртая пара: ' + config.fourparPI60 + ' [' + str(config.kabPI604) + ']\n' + 'Пятая пара: ' + config.fiveparPI60 + ' [' + str(config.kabPI605) + ']\n' + 'Шестая пара: ' + config.sixparPI60 + ' [' + str(config.kabPI606) + ']\n'
    elif call.data == "subb":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на субботу:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparSU60 + ' [' + str(config.kabSU601) + ']\n' + 'Вторая пара: ' + config.twoparSU60 + ' [' + str(config.kabSU602) + ']\n' + 'Третья пара: ' + config.threeparSU60 + ' [' + str(config.kabSU603) + ']\n' + 'Четвёртая пара: ' + config.fourparSU60 + ' [' + str(config.kabSU604) + ']\n' + 'Пятая пара: ' + config.fiveparSU60 + ' [' + str(config.kabSU605) + ']\n' + 'Шестая пара: ' + config.sixparSU60 + ' [' + str(config.kabSU606) + ']\n'
        # Отправляем текст в Телеграм
    bot.send_message(call.message.chat.id, msg)
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)
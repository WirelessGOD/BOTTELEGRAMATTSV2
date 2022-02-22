import config
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot(config.TOKEN58)
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Метод, который получает сообщения и обрабатывает их
print('58 ЗАПУЩЕН')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «/start»
    if message.text == "/start":
        print('+1')
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет. Я создан для того чтобы облегчить тебе жизнь (ГРУППА 58)")
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
        bot.send_message(message.from_user.id, "Привет. Я создан для того чтобы облегчить тебе жизнь (ГРУППА 58)")
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
        msg = 'Первая пара: ' + config.oneparP58 + ' [' + str(config.kabP581) + ']\n' + 'Вторая пара: ' + config.twoparP58 + ' [' + str(config.kabP582) + ']\n' + 'Третья пара: ' + config.threeparP58 + ' [' + str(config.kabP583) + ']\n' + 'Четвёртая пара: ' + config.fourparP58 + ' [' + str(config.kabP584) + ']\n' + 'Пятая пара: ' + config.fiveparP58 + ' [' + str(config.kabP585) + ']\n' + 'Шестая пара: ' + config.sixparP58 + ' [' + str(config.kabP586) + ']\n'
    elif call.data == "vtr":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на вторник:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparV58 + ' [' + str(config.kabV581) + ']\n' + 'Вторая пара: ' + config.twoparV58 + ' [' + str(config.kabV582) + ']\n' + 'Третья пара: ' + config.threeparV58 + ' [' + str(config.kabV583) + ']\n' + 'Четвёртая пара: ' + config.fourparV58 + ' [' + str(config.kabV584) + ']\n' + 'Пятая пара: ' + config.fiveparV58 + ' [' + str(config.kabV585) + ']\n' + 'Шестая пара: ' + config.sixparV58 + ' [' + str(config.kabV586) + ']\n'
    elif call.data == "srd":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на среду:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparS58 + ' [' + str(config.kabS581) + ']\n' + 'Вторая пара: ' + config.twoparS58 + ' [' + str(config.kabS582) + ']\n' + 'Третья пара: ' + config.threeparS58 + ' [' + str(config.kabS583) + ']\n' + 'Четвёртая пара: ' + config.fourparS58 + ' [' + str(config.kabS584) + ']\n' + 'Пятая пара: ' + config.fiveparS58 + ' [' + str(config.kabS585) + ']\n' + 'Шестая пара: ' + config.sixparS58 + ' [' + str(config.kabS586) + ']\n'
    elif call.data == "chet":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на четверг:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.onepar458 + ' [' + str(config.kab4581) + ']\n' + 'Вторая пара: ' + config.twopar458 + ' [' + str(config.kab4582) + ']\n' + 'Третья пара: ' + config.threepar458 + ' [' + str(config.kab4583) + ']\n' + 'Четвёртая пара: ' + config.fourpar458 + ' [' + str(config.kab4584) + ']\n' + 'Пятая пара: ' + config.fivepar458 + ' [' + str(config.kab4585) + ']\n' + 'Шестая пара: ' + config.sixpar458 + ' [' + str(config.kab4586) + ']\n'
    elif call.data == "piat":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на пятницу:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparPI58 + ' [' + str(config.kabPI581) + ']\n' + 'Вторая пара: ' + config.twoparPI58 + ' [' + str(config.kabPI582) + ']\n' + 'Третья пара: ' + config.threeparPI58 + ' [' + str(config.kabPI583) + ']\n' + 'Четвёртая пара: ' + config.fourparPI58 + ' [' + str(config.kabPI584) + ']\n' + 'Пятая пара: ' + config.fiveparPI58 + ' [' + str(config.kabPI585) + ']\n' + 'Шестая пара: ' + config.sixparPI58 + ' [' + str(config.kabPI586) + ']\n'
    elif call.data == "subb":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на субботу:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparSU58 + ' [' + str(config.kabSU581) + ']\n' + 'Вторая пара: ' + config.twoparSU58 + ' [' + str(config.kabSU582) + ']\n' + 'Третья пара: ' + config.threeparSU58 + ' [' + str(config.kabSU583) + ']\n' + 'Четвёртая пара: ' + config.fourparSU58 + ' [' + str(config.kabSU584) + ']\n' + 'Пятая пара: ' + config.fiveparSU58 + ' [' + str(config.kabSU585) + ']\n' + 'Шестая пара: ' + config.sixparSU58 + ' [' + str(config.kabSU586) + ']\n'
        # Отправляем текст в Телеграм
    bot.send_message(call.message.chat.id, msg)
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)
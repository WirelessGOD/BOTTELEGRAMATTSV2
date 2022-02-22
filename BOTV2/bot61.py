import config

# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot(config.TOKEN61)
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Метод, который получает сообщения и обрабатывает их
print('61 ЗАПУЩЕН')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «/start»
    if message.text == "/start":
        print('+1')
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет. Я создан для того чтобы облегчить тебе жизнь (ГРУППА 61)")
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
        bot.send_message(message.from_user.id, "Привет. Я создан для того чтобы облегчить тебе жизнь (ГРУППА 61)")
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
        msg = 'Первая пара: ' + config.oneparP61 + ' [' + str(config.kabP611) + ']\n' + 'Вторая пара: ' + config.twoparP61 + ' [' + str(config.kabP612) + ']\n' + 'Третья пара: ' + config.threeparP61 + ' [' + str(config.kabP613) + ']\n' + 'Четвёртая пара: ' + config.fourparP61 + ' [' + str(config.kabP614) + ']\n' + 'Пятая пара: ' + config.fiveparP61 + ' [' + str(config.kabP615) + ']\n' + 'Шестая пара: ' + config.sixparP61 + ' [' + str(config.kabP616) + ']\n'
    elif call.data == "vtr":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на вторник:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparV61 + ' [' + str(config.kabV611) + ']\n' + 'Вторая пара: ' + config.twoparV61 + ' [' + str(config.kabV612) + ']\n' + 'Третья пара: ' + config.threeparV61 + ' [' + str(config.kabV613) + ']\n' + 'Четвёртая пара: ' + config.fourparV61 + ' [' + str(config.kabV614) + ']\n' + 'Пятая пара: ' + config.fiveparV61 + ' [' + str(config.kabV615) + ']\n' + 'Шестая пара: ' + config.sixparV61 + ' [' + str(config.kabV616) + ']\n'
    elif call.data == "srd":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на среду:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparS61 + ' [' + str(config.kabS611) + ']\n' + 'Вторая пара: ' + config.twoparS61 + ' [' + str(config.kabS612) + ']\n' + 'Третья пара: ' + config.threeparS61 + ' [' + str(config.kabS613) + ']\n' + 'Четвёртая пара: ' + config.fourparS61 + ' [' + str(config.kabS614) + ']\n' + 'Пятая пара: ' + config.fiveparS61 + ' [' + str(config.kabS615) + ']\n' + 'Шестая пара: ' + config.sixparS61 + ' [' + str(config.kabS616) + ']\n'
    elif call.data == "chet":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на четверг:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.onepar461 + ' [' + str(config.kab4611) + ']\n' + 'Вторая пара: ' + config.twopar461 + ' [' + str(config.kab4612) + ']\n' + 'Третья пара: ' + config.threepar461 + ' [' + str(config.kab4613) + ']\n' + 'Четвёртая пара: ' + config.fourpar461 + ' [' + str(config.kab4614) + ']\n' + 'Пятая пара: ' + config.fivepar461 + ' [' + str(config.kab4615) + ']\n' + 'Шестая пара: ' + config.sixpar461 + ' [' + str(config.kab4616) + ']\n'
    elif call.data == "piat":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на пятницу:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparP61 + ' [' + str(config.kabP611) + ']\n' + 'Вторая пара: ' + config.twoparP61 + ' [' + str(config.kabP612) + ']\n' + 'Третья пара: ' + config.threeparP61 + ' [' + str(config.kabP613) + ']\n' + 'Четвёртая пара: ' + config.fourparP61 + ' [' + str(config.kabP614) + ']\n' + 'Пятая пара: ' + config.fiveparP61 + ' [' + str(config.kabP615) + ']\n' + 'Шестая пара: ' + config.sixparP61 + ' [' + str(config.kabP616) + ']\n'
    elif call.data == "subb":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на субботу:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparP61 + ' [' + str(config.kabP611) + ']\n' + 'Вторая пара: ' + config.twoparP61 + ' [' + str(config.kabP612) + ']\n' + 'Третья пара: ' + config.threeparP61 + ' [' + str(config.kabP613) + ']\n' + 'Четвёртая пара: ' + config.fourparP61 + ' [' + str(config.kabP614) + ']\n' + 'Пятая пара: ' + config.fiveparP61 + ' [' + str(config.kabP615) + ']\n' + 'Шестая пара: ' + config.sixparP61 + ' [' + str(config.kabP616) + ']\n'
        # Отправляем текст в Телеграм
    bot.send_message(call.message.chat.id, msg)
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)
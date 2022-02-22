import config
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot(config.TOKEN59)
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Метод, который получает сообщения и обрабатывает их
print('59 ЗАПУЩЕН')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «/start»
    if message.text == "/start":
        print('+1')
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет. Я создан для того чтобы облегчить тебе жизнь (ГРУППА 59)")
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
        bot.send_message(message.from_user.id, "Привет. Я создан для того чтобы облегчить тебе жизнь (ГРУППА 59)")
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
        msg = 'Первая пара: ' + config.oneparP59 + ' [' + str(config.kabP591) + ']\n' + 'Вторая пара: ' + config.twoparP59 + ' [' + str(config.kabP592) + ']\n' + 'Третья пара: ' + config.threeparP59 + ' [' + str(config.kabP593) + ']\n' + 'Четвёртая пара: ' + config.fourparP59 + ' [' + str(config.kabP594) + ']\n' + 'Пятая пара: ' + config.fiveparP59 + ' [' + str(config.kabP595) + ']\n' + 'Шестая пара: ' + config.sixparP59 + ' [' + str(config.kabP596) + ']\n'
    elif call.data == "vtr":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на вторник:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparV59 + ' [' + str(config.kabV591) + ']\n' + 'Вторая пара: ' + config.twoparV59 + ' [' + str(config.kabV592) + ']\n' + 'Третья пара: ' + config.threeparV59 + ' [' + str(config.kabV593) + ']\n' + 'Четвёртая пара: ' + config.fourparV59 + ' [' + str(config.kabV594) + ']\n' + 'Пятая пара: ' + config.fiveparV59 + ' [' + str(config.kabV595) + ']\n' + 'Шестая пара: ' + config.sixparV59 + ' [' + str(config.kabV596) + ']\n'
    elif call.data == "srd":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на среду:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparS59 + ' [' + str(config.kabS591) + ']\n' + 'Вторая пара: ' + config.twoparS59 + ' [' + str(config.kabS592) + ']\n' + 'Третья пара: ' + config.threeparS59 + ' [' + str(config.kabS593) + ']\n' + 'Четвёртая пара: ' + config.fourparS59 + ' [' + str(config.kabS594) + ']\n' + 'Пятая пара: ' + config.fiveparS59 + ' [' + str(config.kabS595) + ']\n' + 'Шестая пара: ' + config.sixparS59 + ' [' + str(config.kabS596) + ']\n'
    elif call.data == "chet":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на четверг:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.onepar459 + ' [' + str(config.kab4591) + ']\n' + 'Вторая пара: ' + config.twopar459 + ' [' + str(config.kab4592) + ']\n' + 'Третья пара: ' + config.threepar459 + ' [' + str(config.kab4593) + ']\n' + 'Четвёртая пара: ' + config.fourpar459 + ' [' + str(config.kab4594) + ']\n' + 'Пятая пара: ' + config.fivepar459 + ' [' + str(config.kab4595) + ']\n' + 'Шестая пара: ' + config.sixpar459 + ' [' + str(config.kab4596) + ']\n'
    elif call.data == "piat":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на пятницу:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparPI59 + ' [' + str(config.kabPI591) + ']\n' + 'Вторая пара: ' + config.twoparPI59 + ' [' + str(config.kabPI592) + ']\n' + 'Третья пара: ' + config.threeparPI59 + ' [' + str(config.kabPI593) + ']\n' + 'Четвёртая пара: ' + config.fourparPI59 + ' [' + str(config.kabPI594) + ']\n' + 'Пятая пара: ' + config.fiveparPI59 + ' [' + str(config.kabPI595) + ']\n' + 'Шестая пара: ' + config.sixparPI59 + ' [' + str(config.kabPI596) + ']\n'
    elif call.data == "subb":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на субботу:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparSU59 + ' [' + str(config.kabSU591) + ']\n' + 'Вторая пара: ' + config.twoparSU59 + ' [' + str(config.kabSU592) + ']\n' + 'Третья пара: ' + config.threeparSU59 + ' [' + str(config.kabSU593) + ']\n' + 'Четвёртая пара: ' + config.fourparSU59 + ' [' + str(config.kabSU594) + ']\n' + 'Пятая пара: ' + config.fiveparSU59 + ' [' + str(config.kabSU595) + ']\n' + 'Шестая пара: ' + config.sixparSU59 + ' [' + str(config.kabSU596) + ']\n'
        # Отправляем текст в Телеграм
    bot.send_message(call.message.chat.id, msg)
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)
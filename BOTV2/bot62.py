import config
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot(config.TOKEN62)
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Метод, который получает сообщения и обрабатывает их
print('62 ЗАПУЩЕН')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «/start»
    if message.text == "/start":
        print('+1')
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет. Я создан для того чтобы облегчить тебе жизнь (ГРУППА 62)")
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
        bot.send_message(message.from_user.id, "Привет. Я создан для того чтобы облегчить тебе жизнь (ГРУППА 62)")
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
        msg = 'Первая пара: ' + config.oneparP62 + ' [' + str(config.kabP621) + ']\n' + 'Вторая пара: ' + config.twoparP62 + ' [' + str(config.kabP622) + ']\n' + 'Третья пара: ' + config.threeparP62 + ' [' + str(config.kabP623) + ']\n' + 'Четвёртая пара: ' + config.fourparP62 + ' [' + str(config.kabP624) + ']\n' + 'Пятая пара: ' + config.fiveparP62 + ' [' + str(config.kabP625) + ']\n' + 'Шестая пара: ' + config.sixparP62 + ' [' + str(config.kabP626) + ']\n'
    elif call.data == "vtr":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на вторник:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparV62 + ' [' + str(config.kabV621) + ']\n' + 'Вторая пара: ' + config.twoparV62 + ' [' + str(config.kabV622) + ']\n' + 'Третья пара: ' + config.threeparV62 + ' [' + str(config.kabV623) + ']\n' + 'Четвёртая пара: ' + config.fourparV62 + ' [' + str(config.kabV624) + ']\n' + 'Пятая пара: ' + config.fiveparV62 + ' [' + str(config.kabV625) + ']\n' + 'Шестая пара: ' + config.sixparV62 + ' [' + str(config.kabV626) + ']\n'
    elif call.data == "srd":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на среду:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparS62 + ' [' + str(config.kabS621) + ']\n' + 'Вторая пара: ' + config.twoparS62 + ' [' + str(config.kabS622) + ']\n' + 'Третья пара: ' + config.threeparS62 + ' [' + str(config.kabS623) + ']\n' + 'Четвёртая пара: ' + config.fourparS62 + ' [' + str(config.kabS624) + ']\n' + 'Пятая пара: ' + config.fiveparS62 + ' [' + str(config.kabS625) + ']\n' + 'Шестая пара: ' + config.sixparS62 + ' [' + str(config.kabS626) + ']\n'
    elif call.data == "chet":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на четверг:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.onepar462 + ' [' + str(config.kab4621) + ']\n' + 'Вторая пара: ' + config.twopar462 + ' [' + str(config.kab4622) + ']\n' + 'Третья пара: ' + config.threepar462 + ' [' + str(config.kab4623) + ']\n' + 'Четвёртая пара: ' + config.fourpar462 + ' [' + str(config.kab4624) + ']\n' + 'Пятая пара: ' + config.fivepar462 + ' [' + str(config.kab4625) + ']\n' + 'Шестая пара: ' + config.sixpar462 + ' [' + str(config.kab4626) + ']\n'
    elif call.data == "piat":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на пятницу:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparPI62 + ' [' + str(config.kabPI621) + ']\n' + 'Вторая пара: ' + config.twoparPI62 + ' [' + str(config.kabPI622) + ']\n' + 'Третья пара: ' + config.threeparPI62 + ' [' + str(config.kabPI623) + ']\n' + 'Четвёртая пара: ' + config.fourparPI62 + ' [' + str(config.kabPI624) + ']\n' + 'Пятая пара: ' + config.fiveparPI62 + ' [' + str(config.kabPI625) + ']\n' + 'Шестая пара: ' + config.sixparPI62 + ' [' + str(config.kabPI626) + ']\n'
    elif call.data == "subb":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_back = types.KeyboardButton(text='Назад')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Расписание на субботу:", reply_markup=keyboard)
        msg = 'Первая пара: ' + config.oneparSU62 + ' [' + str(config.kabSU621) + ']\n' + 'Вторая пара: ' + config.twoparSU62 + ' [' + str(config.kabSU622) + ']\n' + 'Третья пара: ' + config.threeparSU62 + ' [' + str(config.kabSU623) + ']\n' + 'Четвёртая пара: ' + config.fourparSU62 + ' [' + str(config.kabSU624) + ']\n' + 'Пятая пара: ' + config.fiveparSU62 + ' [' + str(config.kabSU625) + ']\n' + 'Шестая пара: ' + config.sixparSU62 + ' [' + str(config.kabSU626) + ']\n'
        # Отправляем текст в Телеграм
    bot.send_message(call.message.chat.id, msg)
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)
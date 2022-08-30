import telebot
from telebot import types
from model import db, Posts
from parser import Parser

bot = telebot.TeleBot("5597437980:AAGGfVEuYC40KtbfugkTmgP5JyuVSlATi9o")

@bot.message_handler(commands=["start"])
def hello(user):
    markup = types.InlineKeyboardMarkup(row_width=1)
    # button1 = types.KeyboardButton('Чекнуть последние подписки аккаунта!')
    # button2 = types.KeyboardButton('Запомнить последние подписки аккаунта!')
    button3 = types.InlineKeyboardButton('Выбрать курс!(получение ссылок на курс!)', callback_data='check_lessons')
    button1 = types.InlineKeyboardButton('Посмотреть блоки курса(главы курса)!', callback_data='check_blocks')

    markup.add(button3, button1)
    bot.send_message(user.chat.id, text="Вас приветсвует бот,"
                                        " чекающий курсы и их блоки! "
                                        , reply_markup=markup)


# @bot.message_handler(text='Выбрать курс!(получение ссылок на курс!)')
# def write_user(message: types.Message):
#     f = open('urls_to_learn', 'r')
#     text = f.read()
#     bot.send_message(message.chat.id, text, reply_markup=None)

@bot.callback_query_handler(func=lambda c: c.data == 'check_lessons')
def show_lessons(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    f = open('urls_to_learn', 'r')
    text = f.read()
    bot.send_message(callback_query.from_user.id, text)

@bot.callback_query_handler(func=lambda c: c.data == 'check_blocks')
def select_int(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    text = 'Напишите номер курса!(1, 2, 3, 4, 5, 6)'
    bot.send_message(callback_query.message.chat.id, text)

@bot.message_handler(content_types=['text'])
def show_blocks(message):
    a = Parser()
    b = a.urls_and_check(message)
    bot.send_message(message.chat.id, text=b)









bot.infinity_polling()



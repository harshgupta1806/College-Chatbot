from telebot import types

from connection_bot import make_connection

bot = make_connection()


def make_keyboard(data):
    markup = types.InlineKeyboardMarkup()
    for b in data:
        # markup.add(types.InlineKeyboardButton(text = b, callback_data=b))
        print("b = ", b)
        markup.add(types.InlineKeyboardButton(text=b.split(':')[1], callback_data=str(b)))
    # markup.add(types.InlineKeyboardButton(text='Not a Student', callback_data='None'))
    return markup


def make_keyboard_for_scheme():
    markup = types.InlineKeyboardMarkup()
    data = ['get_branch_syllabus:First Year', 'get_branch_syllabus:Your Branch', 'get_branch_syllabus:Other']
    for b in data:
        # markup.add(types.InlineKeyboardButton(text = b, callback_data=b))
        print("b = ", b)
        markup.add(types.InlineKeyboardButton(text=b.split(':')[1], callback_data=str(b)))
    # markup.add(types.InlineKeyboardButton(text='Not a Student', callback_data='None'))
    return markup

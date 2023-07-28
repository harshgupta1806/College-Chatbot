import random

import connection_bot as cb
import telegram_button
from constants import constant
from scrapper import scheme_scrapper

# ------------------------------- INITIALIZING BOT ----------------------------------

bot = cb.get_bot()


# ------------------------------- BASIC COMMANDS ---------------------------------


def start(message):
    print('start is working ....... ')
    markup = telegram_button.make_keyboard(constant.branch)
    bot_message_id = bot.send_message(message.chat.id,
                                      text='Hmmmm! It seems like you are a new user! Could you please tell me your '
                                           'branch',
                                      reply_markup=markup)
    return bot_message_id.id


def scheme(user_chat_id):
    print('you are in scheme')
    markup = telegram_button.make_keyboard_for_scheme()
    bot_message_id = bot.send_message(user_chat_id,
                                      text='Could you please specify the branch?',
                                      reply_markup=markup)
    return bot_message_id.id


def greet():
    return random.choice(constant.greeting_replies)


def intro(_id):
    bot.send_message(_id, constant.intro)


# ------------------------------- SEND SYLLABUS -------------------------------

def delay_msg(branch):
    delay_msg = 'Fetching Syllabus of ' + branch.upper()
    return delay_msg


def send_syllabus(id, branch):  # *function name updated from send_syllabus1 to send_syllabus
    urls = scheme_scrapper.get_schemes(branch)
    print(urls)
    msg = 'There you go ....' + "\n\n"
    bot.send_message(id, msg)
    for url in urls.items():
        msg = ''
        result1 = str(url[0])
        result2 = str(url[1])
        msg = msg + result1 + "\n" + result2 + "\n\n"
        bot.send_message(id, msg)
    return msg


def send_syllabus_of_all_branches(message): # * function name updated from send_syllabus (Not of Use)
    # two functions... why?
    for dept in constant.dept_name:
        bot.send_message(message.chat.id, send_syllabus(message, dept))


#  civil
# @bot.message_handler(commands = 'syllabus/civil')
def send_syllabus_civil(message):
    bot.send_message(message.chat.id, delay_msg('civil'))
    send_syllabus(message, 'civil')


# chemical
# # @bot.message_handler(commands='syllabus/chemical')
def send_syllabus_chemical(message):
    bot.send_message(message.chat.id, delay_msg('chemical'))
    send_syllabus(message, 'chemical')


# electrical
# @bot.message_handler(commands='syllabus/electrical')
def send_syllabus_electrical(message):
    bot.send_message(message.chat.id, delay_msg('electrical'))
    send_syllabus(message, 'electrical')


#  ft
# # @bot.message_handler(commands='syllabus/ft')
def send_syllabus_ft(message):
    bot.send_message(message.chat.id, delay_msg('Fire Technology'))
    send_syllabus(message, 'ft')


#  mechanical
# # @bot.message_handler(commands='syllabus/mechanical')
def send_syllabus_mechanical(message):
    bot.send_message(message.chat.id, delay_msg('Mechanical Engineering'))
    send_syllabus(message, 'mechanical')


#  cse
def send_syllabus_cse(message):
    bot.send_message(message.chat.id, delay_msg('COMPUTER SCIENCE'))
    send_syllabus(message, 'cse_csit')


# ------------------------- INLINE KEYBOARDS FOR SCHEME AND NOTICE ------------------------------------

def scheme_keyboard(message_id):
    print('Making keyboard .... ')
    markup = telegram_button.make_keyboard(constant.other_syllabus)
    message = bot.send_message(message_id, text="Please tell me your branch..", reply_markup=markup)
    return message.id


def other_notice_keyboard(message_id):
    print('Making keyboard .... ')
    markup = telegram_button.make_keyboard(constant.other_notice)
    message = bot.send_message(message_id, text="So exactly which branch's syllabus your are looking for..",
                               reply_markup=markup)
    return message.id


def notice_keyboard(user_chat_id):
    print('Making Notice keyboard')
    markup = telegram_button.make_keyboard(constant.get_notice)
    bot.send_message(user_chat_id, text='|=====[ Notice-Board ]=====|', reply_markup=markup)


# ------------------------------------------------------------------------

def menu_keyboard(message):
    print('making keyboard for menu')
    markup = telegram_button.make_keyboard(constant.menu)
    bot.send_message(message.chat.id, text="|=====[ MENU ]=====|", reply_markup=markup)

# create connection with telegram

import constants.constant as cc
import telebot


def make_connection():
    global bot
    try:
        bot = telebot.TeleBot(cc.API_KEY)
        print("Successfully connected to telegram.")
        print(__name__)
    except Exception as e:
        print(f"Error: {e}")
    return bot


def get_bot():
    global bot
    return bot
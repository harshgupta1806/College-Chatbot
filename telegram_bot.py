from main import *

if __name__ == '__main__':
    global bot
    try:
        # create the connection
        bot = cb.get_bot()
        print('Bot Started')
        # start the bot
        bot.set_webhook()
        print('bot after webhook')
        bot.infinity_polling()
    except Exception as e:
        print(f"Error occurred: {e}")

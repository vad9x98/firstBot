from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import sett


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                     level=logging.INFO,
                     filename='bot.log')

def greet_user(update: Updater, context: CallbackContext):
    text = 'Привет, добро пожаловать в мой собственный бот'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(update: Updater, context: CallbackContext):
    user_text = 'Привет {}! Ты написал {}'.format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, Chat_id: %s, Message: %s', update.message.chat.username,
                 update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(sett.API_KEY, request_kwargs=sett.PROXY)
    logging.info('Запуск бота')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()
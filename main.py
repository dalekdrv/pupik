from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from secrets import BOT_TOKEN


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def greeting(update, context):
    print('Вызвана команда /start')
    update.message.reply_text('Вызвана команда /start')


def main():
    my_bot = Updater(BOT_TOKEN, use_context=True)

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('start', greeting))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    my_bot.start_polling()
    my_bot.idle()


if __name__ == '__main__':
    main()

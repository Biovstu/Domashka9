from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def hi_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')

updater = Updater('5332535441:AAHmyrfr4G0zsUsZpA5YuK77rl838dlIxGA')
updater.dispatcher.add_handler(CommandHandler('hi', hi_command))

print('server start')
updater.start_polling()
updater.idle()
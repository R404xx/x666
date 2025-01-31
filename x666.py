from flask import Flask
from threading import Thread
from telegram import Update, ChatPermissions
from telegram.ext import Updater, CommandHandler, CallbackContext
import os


app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Your bot code
TOKEN = os.getenv('7902749270:AAFEPfBN0W-9O6pyrRQXvSe_EVjRagiLDUU')  

def start_bot():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Add command handlers
    def mute(update: Update, context: CallbackContext):
        chat_id = update.message.chat_id
        user_id = update.message.reply_to_message.from_user.id
        context.bot.restrict_chat_member(
            chat_id=chat_id,
            user_id=user_id,
            permissions=ChatPermissions(can_send_messages=False)
        )
        update.message.reply_text(f"User {user_id} MUTED.")

    def ban(update: Update, context: CallbackContext):
        chat_id = update.message.chat_id
        user_id = update.message.reply_to_message.from_user.id
        context.bot.ban_chat_member(chat_id=chat_id, user_id=user_id)
        update.message.reply_text(f"User {user_id} banned.")

    def start(update: Update, context: CallbackContext):
        update.message.reply_text("Hello! La Layan @phonix_kbs drust krawm karm mute u banda")

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("mute", mute))
    dispatcher.add_handler(CommandHandler("ban", ban))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":

    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    
    start_bot()

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters
import os
token = os.getenv("BOT_TOKEN")

async def unknown(update, context):
    await update.message.reply_text(
        "Unknown Command ⚠️"
    )

async def start(update, context):
    await update.message.reply_text(
        "Hello {} 👋".format(update.message.from_user.first_name)
    )

def main():
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.COMMAND | filters.TEXT, unknown))

    application.run_polling()

if __name__ == "__main__":

    main()

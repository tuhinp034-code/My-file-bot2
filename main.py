import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from telegram import Update
from telegram.ext import ContextTypes

# HARDCODE YOUR VALUES HERE
TOKEN = "8605688893:AAFF..."  # Paste your token here inside the quotes
CHANNEL_ID = -100433499388    # Paste your channel ID here (no quotes)

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await context.bot.forward_message(
        chat_id=CHANNEL_ID,
        from_chat_id=update.effective_chat.id,
        message_id=update.message.message_id
    )
    link = f"https://t.me/c/{str(CHANNEL_ID)[4:]}/{msg.message_id}"
    await update.message.reply_text(f"File saved! Link: {link}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.Document.ALL | filters.PHOTO | filters.VIDEO, handle_file))
    app.run_polling()

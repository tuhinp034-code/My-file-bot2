import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Replace with your actual credentials
TOKEN = "8605688893:AAFFTwi2HiyB4FKRWKLCXVhX91nfqa4bjZ4"
CHANNEL_ID = -1004334993882

# Setup logging to see exactly what happens in the Railway console
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Forward the message to your channel
        msg = await context.bot.forward_message(
            chat_id=CHANNEL_ID,
            from_chat_id=update.effective_chat.id,
            message_id=update.message.message_id
        )
        # Generate the permanent link
        link = f"https://t.me/c/{str(CHANNEL_ID)[4:]}/{msg.message_id}"
        await update.message.reply_text(f"File saved successfully!\nLink: {link}")
    except Exception as e:
        logging.error(f"Error forwarding file: {e}")
        await update.message.reply_text("Error: Ensure the bot is an admin in the channel.")

if __name__ == '__main__':
    print("Bot is initializing...")
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Handle all file/media types
    file_handler = MessageHandler(filters.Document.ALL | filters.PHOTO | filters.VIDEO, handle_file)
    app.add_handler(file_handler)
    
    print("Bot is now running and polling for updates...")
    app.run_polling()

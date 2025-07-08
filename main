from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == 'private':
        await update.message.reply_text("Terima kasih! Pesan kamu sudah kami terima 😊")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

print("Bot aktif di Railway...")
app.run_polling()

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKENBOT_TOKEN="8914458372:AAGPtSPLyR-1im-imn6lhPD9ZR4K9gvhBHE"*

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎌 Salom! Anime botga xush kelibsiz.\n\n"
        "/anime - Anime tavsiyasi"
    )

async def anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🍿 Tavsiya:\n"
        "• Naruto\n"
        "• One Piece\n"
        "• Attack on Titan\n"
        "• Demon Slayer\n"
        "• Jujutsu Kaisen"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("anime", anime))

app.run_polling()

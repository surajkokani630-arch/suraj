from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8273446422:AAFsAKj-Fmho-NFkTwH1IChlmAIHJfSNnI8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 FOLLOWER WALA BOT69\n\n"
        "💳 UPI: surajdevil93@fam\n"
        "👤 Admin: @ABOUTx_xME\n\n"
        "Payment karne ke baad screenshot admin ko bhej dein."
    )

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot Started...")
app.run_polling()

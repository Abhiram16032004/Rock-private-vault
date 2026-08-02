from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔒 Welcome to Rock Private Vault!\n\nUse /login <PIN> to unlock."
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()

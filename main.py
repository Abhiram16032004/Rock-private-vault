import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔒 Welcome to Rock Private Vault!\n\nUse /login <PIN> to unlock."
    )

async def login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /login <PIN>")
        return

    pin = context.args[0]

    if pin == "2004":
        await update.message.reply_text("✅ Login Successful!")
    else:
        await update.message.reply_text("❌ Wrong PIN!")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("login", login))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

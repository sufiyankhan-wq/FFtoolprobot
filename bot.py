import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_NAME = "FF Tool Pro Bot"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    keyboard = [
        [InlineKeyboardButton("🎮 Free Fire Tools", callback_data="tools")],
        [
            InlineKeyboardButton("🆔 My ID", callback_data="myid"),
            InlineKeyboardButton("⚡ Bot Status", callback_data="status"),
        ],
        [InlineKeyboardButton("📚 Help", callback_data="help")],
        [InlineKeyboardButton("ℹ️ About", callback_data="about")],
    ]

    await update.message.reply_text(
        f"🔥 Welcome, {user.first_name}!\n\n"
        f"🤖 Welcome to {BOT_NAME}!\n\n"
        "Yahan tumhe Free Fire se related useful information milegi.\n\n"
        "👇 Neeche menu se option chuno:",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "tools":
        text = (
            "🎮 FREE FIRE TOOLS\n\n"
            "Yahan future mein useful Free Fire features add karenge.\n"
            "Abhi /help se available commands dekho."
        )
    elif query.data == "myid":
        text = f"🆔 Tumhari Telegram ID: {query.from_user.id}"
    elif query.data == "status":
        text = "🟢 FF Tool Pro Bot chal raha hai!"
    elif query.data == "help":
        text = (
            "📚 COMMANDS\n\n"
            "/start - Welcome Menu\n"
            "/help - Commands list\n"
            "/id - Telegram ID\n"
            "/about - Bot information"
        )
    elif query.data == "about":
        text = "🤖 FF Tool Pro Bot\n🎮 Free Fire community ke liye banaya gaya."
    else:
        text = "Option available nahi hai."

    await query.message.reply_text(text)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 Commands:\n"
        "/start - Welcome Menu\n"
        "/help - Commands list\n"
        "/id - Telegram ID\n"
        "/about - Bot information"
    )


async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🆔 Tumhari Telegram ID: {update.effective_user.id}"
    )


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 FF Tool Pro Bot\n🎮 Free Fire community ke liye banaya gaya."
    )


def main():
    token = os.environ.get("TELEGRAM_BOT_TOKEN") or os.environ

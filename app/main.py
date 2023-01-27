import httpx

from telegram import ForceReply, Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler


# from config import settings

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    first_name = update.message.chat.first_name

    keyboard = [
        [
            KeyboardButton("/audio"),
            KeyboardButton("/text"),
            KeyboardButton("/video"),
        ],
        [KeyboardButton("/image")],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)

    await update.message.reply_text(f"Hi {first_name}, nice to meet you! \nWhat do you want convert?",
                                    reply_markup=reply_markup)


async def audio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            KeyboardButton("/MP4toMP3"),
            KeyboardButton("/MP3toMp4"),

        ],
        [
            KeyboardButton("/AudioToText")
        ]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)

    await update.message.reply_text(f"How do you want convert?",
                                    reply_markup=reply_markup)


async def text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            KeyboardButton("/Txt_To_Pdf"),
            KeyboardButton("/Txt_To_DocX"),

        ],
        [
            KeyboardButton("/TextToAudio")
        ]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)

    await update.message.reply_text(f"How do you want convert?",
                                    reply_markup=reply_markup)


async def my_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(user['id'])


def main() -> None:
    TOKEN = ''
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("my_id", my_id))
    application.add_handler(CommandHandler("audio", audio))
    application.add_handler(CommandHandler("text", text))

    application.run_polling()


if __name__ == "__main__":
    main()

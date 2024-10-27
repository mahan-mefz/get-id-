from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

# توکن API که از BotFather دریافت کردید
TOKEN = "7265077932:AAGiNOR3moqUM1pPMAgaFta6gJJrJWX2Xlk"

# آیدی تلگرام شخصی که می‌خواهید آیدی کاربران به او ارسال شود
TARGET_CHAT_ID = "mahan_mefz"

# تابعی که وقتی کاربر روی /start کلیک کند اجرا می‌شود
def start(update: Update, context: CallbackContext):
    # آیدی کاربر که روی start کلیک کرده است
    user_id = update.message.chat.id
    user_name = update.message.from_user.username

    # ارسال پیغام به چت هدف
    context.bot.send_message(
        chat_id=TARGET_CHAT_ID,
        text=f"کاربر جدید با آیدی @{user_name} و آی‌دی {user_id} دکمه استارت را فشرد."
    )

    # پاسخ به کاربر
    update.message.reply_text("سلام! خوش آمدید به بات.")

def main():
    # ایجاد آپدیت‌کننده و قرار دادن توکن بات
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # هندلر برای دستور /start
    dispatcher.add_handler(CommandHandler("start", start))

    # شروع بات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
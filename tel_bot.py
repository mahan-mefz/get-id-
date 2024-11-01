from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, CallbackContext

# توکن API که از BotFather دریافت کردید
TOKEN = '7150674908:AAFdh3DRd04dVAKyV7pqC8usxPpdkhQQIhE'

# آیدی تلگرام شخصی که می‌خواهید آیدی کاربران به او ارسال شود
TARGET_CHAT_MAHAN = '7821777794'

# تابعی که وقتی کاربر روی /start کلیک کند اجرا می‌شود
async def start(update: Update, context: CallbackContext):
    # آیدی کاربر که روی start کلیک کرده است
    user_id = update.message.chat.id
    user_name = update.message.from_user.username

    # ارسال پیغام به چت هدف
    await context.bot.send_message(
        chat_id=TARGET_CHAT_MAHAN,

        text=f"کاربر جدید با آیدی @{user_name} و آی‌دی {user_id} دکمه استارت را فشرد."
    )

    # پاسخ به کاربر
    await update.message.reply_text(""" به دلیل اختلال در سرور ها فلیم ها و نود ها کمی با تاخیر ارسال میشود """)

def main():
    # ایجاد Application با توکن
    application = Application.builder().token(TOKEN).build()

    # هندلر برای دستور /start
    application.add_handler(CommandHandler("start", start))

    # شروع بات
    application.run_polling()

if __name__ == '__main__':
    main()
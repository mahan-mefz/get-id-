from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, CallbackContext

# توکن API که از BotFather دریافت کردید
TOKEN = '7265077932:AAGiNOR3moqUM1pPMAgaFta6gJJrJWX2Xlk'

# آیدی تلگرام شخصی که می‌خواهید آیدی کاربران به او ارسال شود
TARGET_CHAT_ID = '6169702790'

# تابعی که وقتی کاربر روی /start کلیک کند اجرا می‌شود
async def start(update: Update, context: CallbackContext):
    # آیدی کاربر که روی start کلیک کرده است
    user_id = update.message.chat.id
    user_name = update.message.from_user.username

    # ارسال پیغام به چت هدف
    await context.bot.send_message(
        chat_id=TARGET_CHAT_ID,
        text=f"کاربر جدید با آیدی @{user_name} و آی‌دی {user_id} دکمه استارت را فشرد."
    )

    # پاسخ به کاربر
    await update.message.reply_text("""آیا آماده‌اید تا در جستجوی طلا به بزرگترین کاشف گنج تبدیل شوید؟ 🤩 این یک بازی هیجان‌انگیز تلگرامی است که شما را وارد دنیای چالش‌های جدید و ماجراجویی‌های جذاب می‌کند! 🎉

👑 GOLD DIGGER GAME به شما این فرصت را می‌دهد تا با جستجو و جمع‌آوری طلا، به بالاترین امتیاز دست پیدا کنید و رقبای خود را پشت سر بگذارید. در این بازی شما با هر کلیک به طلا نزدیک‌تر می‌شوید و برای کسب گنجینه‌های بزرگ‌تر رقابت می‌کنید. پس اگر به دنبال هیجان، رقابت و گنج‌های ارزشمند هستید، همین حالا بازی را شروع کنید و ببینید تا کجا می‌توانید پیش بروید!

👥 برای شروع، کافیست این بازی را برای دوستان خود ارسال کنید تا با هم به دنیای ماجراجویی‌های طلایی قدم بگذارید!""")

def main():
    # ایجاد Application با توکن
    application = Application.builder().token(TOKEN).build()

    # هندلر برای دستور /start
    application.add_handler(CommandHandler("start", start))

    # شروع بات
    application.run_polling()

if __name__ == '__main__':
    main()
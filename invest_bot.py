import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

main_menu = ReplyKeyboardMarkup([
    ["📊 سوق البورصة المصرية"],
    ["📈 أسهم الاستثمار"],
    ["📉 أسهم المضاربة"],
    ["📦 خارج المقصورة"],
    ["🏗️ القطاعات"],
    ["🔍 تحليل سهم"],
    ["📥 أسهم الاكتتابات"],
    ["💰 توزيعات الأرباح"],
    ["📊 التحليل الفني اليومي"],
    ["📄 التقرير اليومي"]
], resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبًا بك في بوت التحليل الاستثماري 📊\nاختر من القائمة:", reply_markup=main_menu)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "📊 سوق البورصة المصرية":
        await update.message.reply_text("📊 سيتم عرض جميع مؤشرات البورصة المصرية قريبًا.")
    elif text == "📈 أسهم الاستثمار":
        await update.message.reply_text("💼 ترشيحات استثمارية سيتم تفعيلها قريبًا.")
    elif text == "📉 أسهم المضاربة":
        await update.message.reply_text("⚡ ترشيحات مضاربية يومية وأسبوعية قريبًا.")
    elif text == "📦 خارج المقصورة":
        await update.message.reply_text("📦 سيتم عرض قائمة أسهم خارج المقصورة قريبًا.")
    elif text == "🏗️ القطاعات":
        await update.message.reply_text("🏗️ سيتم عرض القطاعات والأسهم التابعة لكل قطاع قريبًا.")
    elif text == "🔍 تحليل سهم":
        await update.message.reply_text("🧠 من فضلك أرسل كود السهم (مثال: ESRS)")
        context.user_data['awaiting_symbol'] = True
    elif text == "📥 أسهم الاكتتابات":
        await update.message.reply_text("📥 سيتم عرض بيانات الاكتتابات قريبًا.")
    elif text == "💰 توزيعات الأرباح":
        await update.message.reply_text("💰 سيتم عرض جدول التوزيعات ومواعيدها قريبًا.")
    elif text == "📊 التحليل الفني اليومي":
        await update.message.reply_text("📊 سيتم تفعيل التحليل الفني اليومي لمؤشرات البورصة قريبًا.")
    elif text == "📄 التقرير اليومي":
        await update.message.reply_text("📄 جاري تجهيز التقرير اليومي بصيغة PDF... (قريبًا)")
    elif context.user_data.get('awaiting_symbol'):
        symbol = text.upper()
        context.user_data['awaiting_symbol'] = False
        await update.message.reply_text(f"🔍 تحليل فني للسهم {symbol}...\n(التحليل سيتم إضافته هنا)")
    else:
        await update.message.reply_text("⚠️ لم أفهم طلبك. اختر من القائمة.")

if __name__ == '__main__':
    TOKEN = os.getenv("TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot is running...")
    app.run_polling()

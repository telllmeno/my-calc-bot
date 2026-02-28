import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Состояния диалога
A, B, C, D, E, F, G = range(7)

# Токен будем брать из переменной окружения (это безопасно)
TOKEN = '8724239028:AAETwHNcID8HKXuSzb0TRBuBe92TdB3PJn0'

async def start_calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Введите количество часов:")
    return A

async def get_a(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['a'] = float(update.message.text)
        await update.message.reply_text("Введите количество заказов:")
        return B
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return A

async def get_b(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['b'] = float(update.message.text)
        await update.message.reply_text("Введите количество размещений:")
        return C
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return B

async def get_c(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['c'] = float(update.message.text)
        await update.message.reply_text("Введите количество размещения Маркета:")
        return D
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return C

async def get_d(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['d'] = float(update.message.text)
        await update.message.reply_text("Введите количество размещения Мороза:")
        return E
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return D

async def get_e(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['e'] = float(update.message.text)
        await update.message.reply_text("Введите количество часов НПО:")
        return F
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return E

async def get_f(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['f'] = float(update.message.text)
        await update.message.reply_text("Введите значение ККС:")
        return G
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return F

async def get_g(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['g'] = float(update.message.text)
        a = context.user_data['a']
        b = context.user_data['b']
        c = context.user_data['c']
        d = context.user_data['d']
        e = context.user_data['e']
        f = context.user_data['f']
        g = context.user_data['g']

        hours = a * 194
        orders = b * 1.48
        raz = c * 1.08
        market = d * 1.05
        freeze = e * 1.26
        npo = f * 194
        kks = orders * g
        total = hours + raz + market + freeze + npo + kks

        await update.message.reply_text(f"Результат расчёта: {total:.2f} ₽")
        return ConversationHandler.END
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return G

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Диалог отменён.")
    return ConversationHandler.END

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот-калькулятор. Используй /calculate для начала расчёта.")

def main():
    application = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('calculate', start_calculate)],
        states={
            A: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_a)],
            B: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_b)],
            C: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_c)],
            D: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_d)],
            E: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_e)],
            F: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_f)],
            G: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_g)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler('start', start))

    print("Бот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()
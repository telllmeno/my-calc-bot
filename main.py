import logging
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, MessageHandler, filters,
    ConversationHandler, ContextTypes
)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Состояния диалога
COMPANY, A_OLD, B_OLD, C_OLD, D_OLD, E_OLD, F_OLD, G_OLD, B_NEW, C_NEW, D_NEW, E_NEW, F_NEW, G_NEW = range(14)

TOKEN = '8724239028:AAETwHNcID8HKXuSzb0TRBuBe92TdB3PJn0'  # замените на свой, если нужно

async def start_calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Начало диалога: выбор компании."""
    await update.message.reply_text(
        "Выберите компанию:\n"
        "1. ООО Смена\n"
        "2. Другие компании\n"
        "Отправьте 1 или 2"
    )
    return COMPANY

async def company_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка выбора компании."""
    text = update.message.text.strip()
    if text == '1':
        context.user_data['company'] = 'smena'
        await update.message.reply_text("Введите количество часов:")
        return A_OLD
    elif text == '2':
        context.user_data['company'] = 'other'
        await update.message.reply_text("Введите количество заказов:")
        return B_NEW
    else:
        await update.message.reply_text("Пожалуйста, введите 1 или 2.")
        return COMPANY

# --- Старая формула (ООО Смена) ---
async def get_a_old(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['a'] = float(update.message.text)
        await update.message.reply_text("Введите количество заказов:")
        return B_OLD
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return A_OLD

async def get_b_old(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['b'] = float(update.message.text)
        await update.message.reply_text("Введите количество размещений:")
        return C_OLD
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return B_OLD

async def get_c_old(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['c'] = float(update.message.text)
        await update.message.reply_text("Введите количество размещения Маркета:")
        return D_OLD
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return C_OLD

async def get_d_old(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['d'] = float(update.message.text)
        await update.message.reply_text("Введите количество размещения Мороза:")
        return E_OLD
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return D_OLD

async def get_e_old(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['e'] = float(update.message.text)
        await update.message.reply_text("Введите количество часов НПО:")
        return F_OLD
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return E_OLD

async def get_f_old(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['f'] = float(update.message.text)
        await update.message.reply_text("Введите значение ККС:")
        return G_OLD
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return F_OLD

async def get_g_old(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
        await update.message.reply_text(f"Результат расчёта (ООО Смена): {total:.2f} ₽")
        return ConversationHandler.END
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return G_OLD

# --- Новая формула (Другие компании) ---
async def get_b_new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['b'] = float(update.message.text)
        await update.message.reply_text("Введите количество размещений:")
        return C_NEW
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return B_NEW

async def get_c_new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['c'] = float(update.message.text)
        await update.message.reply_text("Введите количество размещения Маркета:")
        return D_NEW
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return C_NEW

async def get_d_new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['d'] = float(update.message.text)
        await update.message.reply_text("Введите количество размещения Мороза:")
        return E_NEW
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return D_NEW

async def get_e_new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['e'] = float(update.message.text)
        await update.message.reply_text("Введите количество часов НПО:")
        return F_NEW
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return E_NEW

async def get_f_new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['f'] = float(update.message.text)
        await update.message.reply_text("Введите значение ККС:")
        return G_NEW
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return F_NEW

async def get_g_new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['g'] = float(update.message.text)
        b = context.user_data['b']
        c = context.user_data['c']
        d = context.user_data['d']
        e = context.user_data['e']
        f = context.user_data['f']
        g = context.user_data['g']

        orders = b * 2.96
        raz = c * 2.17
        market = d * 2.1
        freeze = e * 2.52
        npo = f * 388
        kks = orders * g

        total = raz + market + freeze + npo + kks
        await update.message.reply_text(f"Результат расчёта (Другие компании): {total:.2f} ₽")
        return ConversationHandler.END
    except ValueError:
        await update.message.reply_text("Ошибка! Введите число.")
        return G_NEW

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
            COMPANY: [MessageHandler(filters.TEXT & ~filters.COMMAND, company_choice)],
            A_OLD: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_a_old)],
            B_OLD: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_b_old)],
            C_OLD: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_c_old)],
            D_OLD: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_d_old)],
            E_OLD: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_e_old)],
            F_OLD: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_f_old)],
            G_OLD: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_g_old)],
            B_NEW: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_b_new)],
            C_NEW: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_c_new)],
            D_NEW: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_d_new)],
            E_NEW: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_e_new)],
            F_NEW: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_f_new)],
            G_NEW: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_g_new)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler('start', start))

    print("Бот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()

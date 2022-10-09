import logging
from settings import TOKEN_FOR_BOT
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logging = logging.getLogger(__name__)

CHOICE, RATIONAL_ONE, RATIONAL_TWO, OPERATIONS_RATIONAL, OPERATIONS_COMPLEX, COMPLEX_ONE, \
    COMPLEX_TWO = range(7)

def start(update, _):
    update.message.reply_text('Калькулятор: с какими числами хотите сделать операцию?\n'\
        'Команда /stop чтобы прекратить разговор.\n\n')
    update.message.reply_text('1 - рациональные: \n2- комплексные: \n3 - для выхода \n')
    return CHOICE

def choice(update, context):
    user = update.message.from_user
    logger.info('Выбор операции: %s: %s', user.first_name, update.message.text)
    user_choice = update.message.text
    if user_choice in '123':
        if user_choice == '1':
            update.message.reply_text('Введите первое рациональное число')
            return RATIONAL_ONE
        if user_choice == '2':
            context.bot.send_message(update.effective_chat.id, \
                'Введите Re и In первого рационального числа через ПРОБЕЛ: ')
            return COMPLEX_ONE
    else:
        update.message.reply_text('Это не то.\n 1 - для операций с рациональными числами:\
             \n2 - для операций с комплексными числами:')

def rational_one(update, context):
    user = update.message.from_user
    logger.info('Пользователь ввёл число: %s: %s', user.first_name, update.message.text)
    get_rational = update.message.text
    if get_rational.isdigit():
        get_rational = float(get_rational)
        context.user_data['rational_one'] = get_rational
        update.message.reply_text('Введите второе рациональное число')
        return RATIONAL_TWO
    else:
        update.message.reply_text('Нужно ввести число!')

def rational_two(update, context):
    user = update.message.from_user
    logger.info('Пользователь ввёл число: %s: %s', user.first_name, update.message.text)
    get_rational = update.message.text
    if get_rational.isdigit():
        get_rational = float(get_rational)
        context.user_data['rational_two'] = get_rational
        update.message.reply_text('Введите операцию с числами: \n\n+ - для сложения: \n\
            - - для вычитания: \n* - для умножения: \n/ - для деления')
        return OPERATIONS_RATIONAL

def operations_rational(update, context):
    user = update.message.from_user
    logger.info('Пользователь выбрал операцию: %s: %s', user.first_name, update.message.text)
    rational_one = context.user_data.get('rational_one')
    rational_two = context.user_data.get('rational_two')
    user_choice = update.message.text
    if user_choice in '+-/*':
        if user_choice == '+':
            result = rational_one + rational_two
        if user_choice == '-':
            result = rational_one - rational_two
        if user_choice == '*':
            result = rational_one * rational_two
        if user_choice == '/':
            try:
                result = rational_one / rational_two
            except:
                update.message.reply_text('Деление на ноль запрещено!')
        update.message.reply_text(f'Результат: {rational_one} + {rational_two} = {result}')
        return ConversationHandler.END
    else:
        update.message.reply_text('Это не то. Введите +-*/')
    
def complex_one(update, context):
    user = update.message.from_user
    logger.info('Пользователь ввёл число: %s: %s', user.first_name, update.message.text)
    user_choice = update.message.text
    test = user_choice.replace('-', '')
    if ' ' in test and (test.replace(' ', '')).isdigit():
        user_choice = user_choice.split(' ')
        complex_one = complex(int(user_choice[0]), int(user_choice[1]))
        context.user_data['complex_one'] = complex_one
        update.message.reply_text(f'Первое число {complex_one}, \
            Введите Re и In первого числа через ПРОБЕЛ: ')
        return COMPLEX_ONE
    else:
        update.message.reply_text('Это не то. Введите Re и In первого числа через ПРОБЕЛ: ')

def complex_two(update, context):
    user = update.message.from_user
    logger.info('Пользователь ввёл число: %s: %s', user.first_name, update.message.text)
    user_choice = update.message.text
    test = user_choice.replace('-', '')
    if ' ' in test and (test.replace(' ', '')).isdigit():
        user_choice = user_choice.split(' ')
        complex_two = complex(int(user_choice[0]), int(user_choice[1]))
        context.user_data['complex_two'] = complex_two
        update.message.reply_text(f'Второе число {complex_two}, \
            Введите Re и In второго числа через ПРОБЕЛ: ')
        return OPERATIONS_COMPLEX
    else:
        update.message.reply_text('Это не то. Введите Re и In второго числа через ПРОБЕЛ: ')

def operations_complex(update, context):
    user = update.message.from_user
    logger.info('Пользователь выбрал операцию: %s: %s', user.first_name, update.message.text)
    complex_one = context.user_data.get('complex_one')
    complex_two = context.user_data.get('complex_two')
    user_choice = update.message.text
    if user_choice in '+-/*':
        if user_choice == '+':
            result = complex_one + complex_two
        if user_choice == '-':
            result = complex_one - complex_two
        if user_choice == '*':
            result = complex_one * complex_two
        if user_choice == '/':
            try:
                result = complex_one / complex_two
            except:
                update.message.reply_text('Деление на ноль запрещено!')
        update.message.reply_text(f'Результат: {complex_one} + {complex_two} = {result}')
        return ConversationHandler.END
    else:
        update.message.reply_text('Это не то. Введите +-*/')

def stop(update, _):
    user = update.message.from_user
    logger.info('Пользователь %s отменил разговор.', user.first_name)
    update.message.reply_text('Разговор закончен')
    return ConversationHandler.END

if __name__ == '__main__':
    updater = Updater(TOKEN_FOR_BOT)
    dispatcher = updater.dispatcher
    conversation_handler = ConversationHandler(entry_points=[CommandHandler('start', start)], states={
        CHOICE: [MessageHandler(Filters.text, choice)],
        RATIONAL_ONE: [MessageHandler(Filters.text, rational_one)],
        RATIONAL_TWO: [MessageHandler(Filters.text, rational_two)],
        OPERATIONS_RATIONAL: [MessageHandler(Filters.text, operations_rational)],
        OPERATIONS_COMPLEX: [MessageHandler(Filters.text, operations_complex)],
        COMPLEX_ONE: [MessageHandler(Filters.text, complex_one)],
        COMPLEX_TWO: [MessageHandler(Filters.text, complex_two)],
    },

    fallbacks=[CommandHandler('stop', stop)]
    )

    dispatcher.add_handler(conversation_handler)

    updater.start_polling()

    updater.idle()

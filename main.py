import telebot
from bot_logic import gen_pass

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['gen_pass'])
def send_pass(message):
    words = message.text.split()
    if len(words) > 1:
        l = int(words[1])
        bot.send_message(message.chat.id, gen_pass(l))
    else:
        bot.send_message(message.chat.id, 'нужно указать длину пароля')

    
# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)


@bot.message_handler(commands=['info', 'help'])
def on_info(message):

    bot.reply_to(message, 'привет я бот помогаю тут иногда,напиши /heh чтобы похихикать')

bot.polling()
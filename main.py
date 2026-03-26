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
    bot.reply_to(message, gen_pass(length = 7))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_messange(message.chat.id, message.text)

bot.polling()
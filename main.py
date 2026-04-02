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

@bot.message_handler(func=lambda m: True, content_types=['new_chat_members'])
def on_user_joins(message):
    for user in message.new_chat_members:

        name = user.first_name
        if hasattr(user, 'last_name') and user.last_name is not None:
            name += u" {}".format(user.last_name)

        if hasattr(user, 'username') and user.username is not None:
            name += u" (@{})".format(user.username)

        bot.reply_to(message, 'хеллоу {name}'.format(name=name))


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

    bot.reply_to(message, 'привет я бот помогаю тут иногда ээээ,напиши /heh чтобы похихикать или /joke чтобы увидеть несмешной анекдот ок')


@bot.message_handler(commands=['joke'])
def send_joke(message):

    bot.reply_to(message, 'купил физрук шляпу,а она еиу как раз два раз два раз два')


@bot.message_handler(commands=['meme'])
def send_meme(message):
    with open('images/Горячий песок.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  


bot.polling()
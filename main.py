import telebot
import config

bot = telebot.TeleBot(config.API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Добро пожаловать в онлайн-школу!")

@bot.message_handler(content_types = ['text'])
def handle_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет')

bot.infinity_polling()
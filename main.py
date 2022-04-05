import telebot
from telebot import types
from Application import Application
import config

app = Application()
bot = telebot.TeleBot(config.API_KEY)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)




@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    loginBtn = types.KeyboardButton("Вход")
    infoBtn = types.KeyboardButton("Информация о школе")
    markup.add(loginBtn, infoBtn)
    bot.send_message(message.chat.id, text="Добро пожаловать в онлайн-школу!", reply_markup=markup)

@bot.message_handler(content_types = ['text'])
def handle_message(message):
    msg =  message.text.lower()
    if msg == 'вход':
        handle_login(message)
    elif msg == 'информация о школе':
        show_information(message)
        

def show_information(message):
    bot.send_message(message.chat.id, app.school.displayInfo(), reply_markup=markup)

def handle_login(message):
    bot.send_message(message.chat.id, "Введите логин")
    
    

bot.infinity_polling()
import telebot
import random
from BOTDB import *
bot = telebot.TeleBot("TOKEN")

print("Running!")

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'OwO')
    
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'hello' or message.text.lower() == 'hi':
        bot.send_message(message.from_user.id, random.choice(hello))
        
    elif message.text.lower() == 'i love you':
        bot.send_message(message.from_user.id, love)
        
    elif message.text.lower() == 'why':
        bot.send_message(message.from_user.id, random.choice(why))
        
    elif message.text.lower() == 'cookie':
        bot.send_message(message.from_user.id, random.choice(qst))
        
    elif message.text.lower() == 'yes or no?':
        bot.send_message(message.from_user.id, random.choice(yesNo))

    elif message.text.lower() == 'bye':
        bot.send_message(message.from_user.id, random.choice(bye))
        
    else:
        bot.send_message(message.from_user.id, random.choice(dontUnderstand))

@bot.message_handler(content_types=['sticker'])
def get_sticker_messages(message):
    bot.send_message(message.from_user.id, random.choice(stk))
    
bot.polling(none_stop=True)

import telebot
import random
from BOTDB import qst, yn, stk, hello, love, why
bot = telebot.TeleBot("TOKEN")

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
        bot.send_message(message.from_user.id, random.choice(yn))
        
    else:
        bot.send_message(message.from_user.id, 'UNRECOGNIZABLE ERROR')

@bot.message_handler(content_types=['sticker'])
def get_sticker_messages(message):
    bot.send_message(message.from_user.id, random.choice(stk))
    
bot.polling(none_stop=True)

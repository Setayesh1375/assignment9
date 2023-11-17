import random
import telebot
from telebot import types

my_keyboard = type.ReplyKeyboardMarkup(row_width = 3)
key1 = types.keyboardButton("برگشت به عقب")
key2 = types.keyboardButton("فال حافظ")
key3 = types.keyboardButton("ماشین حساب  ")
key4 = types.keyboardButton("  راهنما")
key5 = types.keyboardButton("چت بات  ")
key6 = types.keyboardButton("  دانلود")

my_keyboard.add(key1 , key2 , key3 , key4 , key5 , key6)



bot = telebot.TeleBot("6957516350:AAHtsKGsHLTsnz2RHpQFvGOjprsy1frPe3Q", parse_mode=None)



@bot.message_handler(commands= ["fal"])
def send_fal(message):
    fal_list = ["شخص بزرگی را خواهی دید","به دیدار یار خواهی رفت","به سفر خواهی رفت"]
    selected_fal = random.choice(fal_list)
    bot.send_message(message.chat.id, selected_fal)   


	
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "سلام خوش اومدین")
	


@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "چه کمکی از دستم برمیاد")
		

@bot.message_handler(func=lambda m: True)
def echo_all(message):
		if message.text == "سلام":
			bot.send_message(message.chat.id, "سلام عزیز")
		elif message.text =="خوبی؟" : 
			bot.send_message(message.chat.id, "ممنونم عزیز")
		elif message.text =="دوستت دارم" : 
			bot.send_message(message.chat.id,"منم")
		elif message.text == "عکس قدی بده" : 
				photo =open("assignment9/1.jpg" , "rb")
				bot.send_photo(message.chat.id , photo)
		else:
			bot.send_message(message.chat.id, "نمیفهمم داری چی میگی!" , reply_markup = my_keyboard)



bot.infinity_polling()
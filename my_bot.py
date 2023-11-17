import random
import qrcode
import gtts
import khayyam
import telebot
from telebot import types



bot = telebot.TeleBot("6957516350:AAHtsKGsHLTsnz2RHpQFvGOjprsy1frPe3Q", parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "سلام خوش اومدین")




@bot.message_handler(commands=['game'])
def computer_number(message):
	global new_number
	new_number = random.randint(0,100)
	bot.send_message(message.chat.id,"به بازی حدس عدد خوش اومدی"+"\n   یک عدد بین 0 تا 100 انتخاب کن")
@bot.message_handler(func=lambda m: True)
def user_number(message):
    if new_number > int(message.text) :
        bot.send_message(message.chat.id ," برو بالا ")
    elif new_number < int(message.text) :
        bot.send_message(message.chat.id , "بیا پایین ") 
    elif new_number == int(message.text) :
        bot.send_message(message.chat.id , " برنده شدی", reply_markup=markup)





@bot.message_handler(commands=['age'])
@bot.message_handler(func=lambda m: True)
def age(message):
    
    bot.send_message(message.chat.id, "تاریخ تولدت رو وارد کن")
    date_of_birth = message.text.split("/")
    dif=khayyam.JalaliDate.today()-khayyam.JalaliDate(date_of_birth[0], date_of_birth[1], date_of_birth[2])
    year = dif // 365
    month = (dif - (year * 365)) // 30
    day = dif - (year * 365 + month * 30)
    
    bot.send_message (message.chat.id,+ year + " و " + month + " و " + day + )





		
@bot.message_handler(commands=['voice'])
@bot.message_handler(func=lambda m: True)
def voice(message):
    input=bot.send_message(message.chat.id, "جمله‌ی خود را به انگلیسی وارد کنید.")
    v = gtts.gTTS (input, lang= 'en', slow = False)
    v.save ("assignment9/voice.mp3")
    audio = open('D:\voice.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)



@bot.message_handler(commands=['argmax'])
@bot.message_handler(func=lambda m: True)
def max_number_list(message):
    user_number2 = str(message.text)
    numbers = user_number2.split(" ")    
    list_number=[]
    for number in numbers :
        list_number.append(number)
    n=max(list_number)
    bot.reply_to(message,n , reply_markup=markup)





@bot.message_handler(commands=['QRcode'])
def crating_QRcode(message):
	text = bot.send_message(message.chat.id, "جمله ات چیه ؟ ")
	bot.register_next_step_handler(text, crating_QRcode)
def user_text(message):
	QR_text = message.text
	img = qrcode.make(QR_text)
	img.save("qrcode.png")
	QRc = open("qrCode.jpg",'rb')
	bot.send_photo(message.chat.id, QRc, reply_markup=markup)



@bot.message_handler(commands=['help'])
def help_user(message):
	bot.reply_to(message,"گزینه های باتمون شامل :")
	bot.send_message(message.chat.id, "QRcode"
				      	"\n age: "
						"\n voice:"
						"\n max: "
						"\n argmax: "
						"\n help:")



bot.infinity_polling()
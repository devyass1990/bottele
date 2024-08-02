import telebot
import requests , re

token = "7480616950:AAGyi8PuLTDSfTOUtLK6mBK0bzxlAAuOzy4" # توكن
bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda m:True)
def all(message):
    msg = message.text

    if(re.match(r'(.*)@(.*)', msg)):
        username = re.sub('@', '', msg)
        url = "https://t.me/s/" + username + "?before=100"
        res = requests.get(url)
        matches = re.findall(r'<time datetime="(.*?)" class="time">', res.text)
        
        if len(matches) > 0:
            date = matches[0]
            date = date.replace('T', '\nTime: ')
            bot.reply_to(message, "• اهلا بك عزيزي تاريخ انشاء قناتك هو \n" + date)
        else:
            bot.reply_to(message, "قناة غير موجودة")



bot.polling()

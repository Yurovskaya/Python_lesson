import telebot
token = '7029102660:AAEG223FT_cUiK1rTr270j0nn0oCHA5kmps'
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.chat.id, message.text)

bot.infinity_polling()




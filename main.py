import telebot 

bot = telebot.TeleBot("token bots")

@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
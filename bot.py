import telebot

TOKEN = "8989723054:AAFboeoSwNVX9oXEM3FfWs2BVGa7a1nFktM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот.\nКоманды:\n/help - список команд\n/weather - погода (учебный пример)")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "/start - приветствие\n/help - эта справка\n/weather - погода")

@bot.message_handler(commands=['weather'])
def weather(message):
    bot.send_message(message.chat.id, "Сегодня +25°, солнечно (это пример)")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, f"Неизвестная команда. Напишите /help")

if __name__ == "__main__":
    print("Бот запущен")
    bot.infinity_polling()
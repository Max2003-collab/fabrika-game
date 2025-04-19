from flask import Flask, request
import telebot
import os

TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def index():
    return 'Bot is running!'

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton(text="Запустити FABRIKA", web_app=telebot.types.WebAppInfo(url="https://your-webapp-link.com"))
    markup.add(btn)
    bot.send_message(message.chat.id, "Привіт! Натисни кнопку нижче, щоб відкрити FABRIKA.", reply_markup=markup)

if __name__ == '__main__':
    app.run(debug=True)
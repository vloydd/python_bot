from click import command
import telebot
from telebot import types

token = ''
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('FAQ', url='http://bahrainair.dev.drudesk.com/faq'))
    start_message = f"<i>Hello, My Friend {message.from_user.first_name}! Welcome to <tg-spoiler>Bahrain Interntational Airport</tg-spoiler>. I'm Here to Help You</i>"
    markup.add(types.InlineKeyboardButton('Barain International Airport', url='http://bahrainair.dev.drudesk.com/faq'))
    start_message = f"<i>Hello, My Friend {message.from_user.first_name}! Welcome to <tg-spoiler>Bahrain Interntational Airport</tg-spoiler>. I'm Here to Help You</i>"
    bot.send_message(message.chat.id, start_message, parse_mode='html', reply_markup=markup)

@bot.message_handler(commands = ['help'])
def help(message):
    btn = types.ReplyKeyboardMarkup( resize_keyboard = True, row_width = 1)
    corp = types.KeyboardButton('Corporate Page')
    main = types.KeyboardButton('Main Page')
    btn.add(main, corp)
    intro = f'<i>Dear, <b>{message.from_user.first_name}</b> May I help You? My Team Developers: @Taraskorpach, @dana_ostapiuk, @maks_oleksyuk and @vloydd</i>'
    bot.send_message(message.chat.id, intro, parse_mode='html', reply_markup = btn)

@bot.message_handler()
def get_user_text(message):
    if message.text == 'Tell us about yourself':
        myinfo = f'<a href="http://bahrainair.dev.drudesk.com/corporate/bahrain-international-airport">Our Story:</a> With its advanced technology and convenience-oriented approach, the new Passenger Terminal aims to put Bahrain International Airport on the global aviation map alongside the world’s leading smart airports. It was designed to enhance efficiency and security while meeting passengers’ growing expectations for a more seamless airport experience. Advancements in automation streamline some of the most time-consuming processes and procedures, giving passengers more control over their journeys.' 
        photo = open('bac.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, myinfo, parse_mode='html')
    elif message.text == 'Info' or message.text == 'info':
        bot.send_message(message.chat.id, message, parse_mode='html')
    elif message.text == 'geo':
        bot.send_location(message.chat.id, 26.26718666927785, 50.63027404279076)
        bot.send_message(message.chat.id, "Airport is Up There", parse_mode='html')
    elif message.text == 'myID' or message.text == 'myid':
        bot.send_message(message.chat.id, message.from_user.id, parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Don't Understand You(", parse_mode='html')

bot.polling(none_stop=True)
import telebot
from telebot import types
import keybords


bot = telebot.TeleBot('5445825797:AAEpJL0LoGhm66YD0q9mnOikjVvbGkCHnic');




@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Выбрать карту")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я помогу тебе кидать гранаты".format(message.from_user), reply_markup=markup)
   

@bot.message_handler(content_types=['text'])
def choose_map(message):
    message.text == "Выбрать карту"
    msg = bot.send_message(message.chat.id, text="Карта", reply_markup=keybords.map_keyboard)
    bot.register_next_step_handler(msg, map)

def map(message):
    if message.chat.id == 'Overpass':
        msg = bot.send_message(message.chat.id, text="Гранаты на оверпассе", reply_markup=keybords.side_keyboard)
        a1 = 'Overpass'
        bot.register_next_step_handler(msg, choose_side, a1)
    elif message.text == 'Inferno':
        msg = bot.send_message(message.chat.id, text="Гранаты на инферно", reply_markup=keybords.nade_keyboard)
        a1 = 'Inferno'
        bot.register_next_step_handler(msg, choose_side, a1)
    elif message.text == 'Dust2':
        msg = bot.send_message(message.chat.id, text="Гранаты на Даст2", reply_markup=keybords.nade_keyboard)
        a1 = 'Dust2'
        bot.register_next_step_handler(msg, choose_side, a1)
    elif message.text == 'Ancient':
        msg = bot.send_message(message.chat.id, text="Гранаты на Эншенте", reply_markup=keybords.nade_keyboard)
        a1 = 'Ancient'
        bot.register_next_step_handler(msg, choose_side, a1)
    elif message.text == 'Vertigo':
        msg = bot.send_message(message.chat.id, text="Гранаты на Вертиго", reply_markup=keybords.nade_keyboard)
        a1 = 'Vertigo'
        bot.register_next_step_handler(msg, choose_side, a1)
    elif message.text == 'Mirage':
        msg = bot.send_message(message.chat.id, text="Гранаты на Мираже", reply_markup=keybords.nade_keyboard)
        a1 = 'Mirage'
        bot.register_next_step_handler(msg, choose_side, a1)

def choose_side(message, a1):
    if message.chat.id == 'T':
        msg = bot.send_message(message.chat.id, text="Выберите сторону", reply_markup=keybords.plant_keyboard)
        a2 = 'T'
        bot.register_next_step_handler(msg, choose_plant, a1, a2)
    elif message.chat.id == 'CT':
        msg = bot.send_message(message.chat.id, text="Выберите сторону", reply_markup=keybords.plant_keyboard)
        a2 = 'CT'
        bot.register_next_step_handler(msg, choose_plant, a1, a2)

def choose_plant(message, a1, a2):
    if message.chat.id == 'A':
        msg = bot.send_message(message.chat.id, text="Выберите сторону", reply_markup=keybords.nade_keyboard)
        a3 = 'A'
        bot.register_next_step_handler(msg, choose_side, a1, a2, a3)
    elif message.chat.id == 'B':
        msg = bot.send_message(message.chat.id, text="Выберите сторону", reply_markup=keybords.nade_keyboard)
        a3 = 'B'
        bot.register_next_step_handler(msg, choose_nade, a1, a2, a3)


           
def choose_nade(message, a1, a2, a3):
    if message.text == 'Molotov':
        msg = bot.send_message(message.chat.id, text="Сейчас покажу все Молотовы", reply_markup=keybords.over_molotov_keyboard)
        bot.register_next_step_handler(msg, molotov_over)
    elif message.text == 'Smoke':
        bot.send_message(message.chat.id, text="Сейчас покажу все Смоки", reply_markup=keybords.over_molotov_keyboard)
    elif message.text == 'Granade':
        bot.send_message(message.chat.id, text="Сейчас покажу все Гранаты", reply_markup=keybords.over_molotov_keyboard)
    elif message.text == 'Flash':
        bot.send_message(message.chat.id, text="Сейчас покажу все Флешки", reply_markup=keybords.over_molotov_keyboard)






bot.polling(none_stop=True)
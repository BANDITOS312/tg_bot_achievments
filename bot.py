import telebot
from logic import DB_Manager
from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

db_manager = DB_Manager()

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Используйте команду /random для получения случайного достижения или /choose для выбора достижения по имени.")

@bot.message_handler(commands=['random'])
def random_achievement(message):
    achievement = db_manager.get_random_achievement()
    if achievement:
        name, description, need_to_do = achievement
        response = f"Достижение: {name}\nОписание: {description}\nЧто нужно сделать: {need_to_do}"
    else:
        response = "Нет достижений в базе данных."
    
    bot.reply_to(message, response)

@bot.message_handler(commands=['choose'])
def choose_achievement(message):
    bot.reply_to(message, "Пожалуйста, введите название достижения, которое вы хотите выбрать:")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    achievement_name = message.text.strip()
    description = db_manager.get_description_name(achievement_name)
    need_to_do = db_manager.get_NeedToDo_name(achievement_name)

    if description and need_to_do:
        response = f"Достижение: {achievement_name}\nОписание: {description}\nЧто нужно сделать: {need_to_do}"
    else:
        response = "Извините, я не нашел достижение с таким названием."

    bot.reply_to(message, response)

if __name__ == "__main__":
    bot.polling(none_stop=True)

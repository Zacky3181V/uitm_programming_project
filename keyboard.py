from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
b1 = KeyboardButton('Rzeszow')
b2 = KeyboardButton('Krakow')
b3 = KeyboardButton('Warszawa')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.row(b1,b2,b3)
from aiogram import types


button1 = types.KeyboardButton(text="Покажи лису")
button2 = types.KeyboardButton(text="Стоп")
button3 = types.KeyboardButton(text="Инфо")
button4 = types.KeyboardButton(text="Закрыть")

keyboard1 = [
    [button1, button2],
    [button3, button4]
]


kb1= types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
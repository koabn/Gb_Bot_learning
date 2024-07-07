import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import config
from Keyboard import kb1
from random_fox import fox


API_TOKEN = config.token

# Включаем логирование, чтобы видеть сообщения в консоли
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"привет, {name}", reply_markup=kb1)


@dp.message(Command("ура"))
async def send_ura(message: types.Message):
    await message.answer("УРАААА! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его.")


@dp.message(Command("лиса"))
@dp.message(Command("fox"))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f"Держи лису, {name}")
    await message.answer_photo(photo=img_fox)

@dp.message(F.text)
async def echo(message: types.Message):
    msg_user = message.text
    name=message.chat.first_name
    if "Привет" in msg_user:
        await message.answer(F"привет, {name}")
    if "пока" in msg_user:
        await message.answer(F"пока, {name}")
    else:
        await message.answer(f"Я не знаю такого слова")

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
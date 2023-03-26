from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import Message

bot = Bot("6288307219:AAFbMkEihETvSsQrXpSLvjhlJWPhGLKtdQA")
dp = Dispatcher(bot)


async def on_start(_):
    print('Бот запущен')

@dp.message_handler(commands=['start'])
async def com_start(message: Message):
    await message.reply('Бот запущен и готов к работе')

@dp.message_handler()
async def com_start(message: Message):
    if message.text =='молодец':
        await message.reply(f'Спасибо, {message.from_user.first_name},'
                        f'ты тоже')
    elif message.text == 'дурак':
        await message.answer('ой! на себя посмотри')
    elif message.text == '80-60':
        await message.answer('20')


executor.start_polling(dp, skip_updates=True, on_startup=on_start)


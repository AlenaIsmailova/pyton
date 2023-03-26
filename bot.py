
from aiogram import Bot, Dispatcher
from aiogram.utils import executor

bot = Bot("6288307219:AAFbMkEihETvSsQrXpSLvjhlJWPhGLKtdQA")
dp = Dispatcher(bot)

async def on_start(_):
    print('Бот запущен')


executor.start_polling(dp, skip_updates=True, on_startup=on_start)

import random
import config
from create_bot import dp
from aiogram.types import Message




@dp.message_handler(commands=['start', 'начать'])
async def mes_start(message: Message):
    await message.answer(text=f'{message.from_user.first_name}, привет!\n'
                         f'Сегодня мы с тобой поиграем в интересную игру!')

@dp.message_handler(commands=['new'])
async def mes_new_game(message: Message):
    config.total = 150
    await message.answer(text=f'На столе {config.total} конфет.'
                              f'Кидаем жребий, кто начинает первым')
    coin = random.randint(0, 1)
    if coin:
        await message.answer(text=f'{message.from_user.first_name}, поздравляю! '
                                  f'Выпал орел, ты ходишь первым. Бери от 1 до 28 конфет')
    else:
        await message.answer(text=f'{message.from_user.first_name}, не расстраивайся'
                         f'первый ход делает бот!')
        await bot_turn(message)

@dp.message_handler()
async def all_catch(message: Message):
    if message.text.isdigit():
        if 0 < int(message.text) < 29:
            await player_turn(message)
        else:
            await message.answer(text=f'Хитрый {message.from_user.first_name}!'
                                      f'Возьми не больше 28 конфет. Попробуй еще раз')
    else:
        await message.answer(text='Введи цифрами количество конфет')


async def player_turn(message: Message):
    take_amount = int(message.text)
    config.total -= take_amount
    name = message.from_user.first_name
    await message.answer(text=f'{name} взял {take_amount} конфет и на столе осталось {config.total}\n')
    if await check_victory(message, name):
        return
    await message.answer(text=f'Ход бота')
    await bot_turn(message)

async def bot_turn(message: Message):
    take_amount = random.randint(1, 28)
    config.total -= take_amount
    name = message.from_user.first_name
    await message.answer(text=f'Бот взял {take_amount} конфет и на столе осталось {config.total}\n')
    if await check_victory(message, 'Бот'):
        return
    await message.answer(text=f'Твоя очередь')


async def check_victory(message: Message, name: str):
    if config.total <=0:
        await message.answer(text=f'Победил {name}! Хорошая игра')
        return True
    return False
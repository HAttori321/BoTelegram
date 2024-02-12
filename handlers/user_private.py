from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
import random

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message:types.Message):
    await message.answer('Hello, I`m a your personal bot')

@user_private_router.message(Command("menu"))
async def menu_cmd(message:types.Message):
    await message.answer('Menu :\n1. /menu\n 2. /help\n 3. /echo\n 4. /start\n')

@user_private_router.message(Command("echo"))
async def menu_cmd(message:types.Message):
    await message.answer(message.text)

@user_private_router.message(Command("help"))
async def menu_cmd(message:types.Message):
    await message.answer("Hello im a new bot and i want  to you")

@user_private_router.message((F.photo)| F.text().contains("кажі"))
async def photo_mess(message:types.Message):
    await message.answer("I understand that it`s photo but i can`t explain it!")

@user_private_router.message()
async def echo(message:types.Message):
    listOfPhrase = ['hi','hello','привіт','здоров','здоровенькі були','здоровенькі']
    randChoice = random.choice(listOfPhrase)
    text = message.text.lower()
    if text in ['hi','hello','привіт','здоров','здоровенькі були','здоровенькі']:
        await message.answer(randChoice)
    elif text in ['bye','goodbye','пока','до побачення','до побачення','до побачення','до побачення']:
        await message.answer('Goodbye, my friend')
    else:
        await message.answer("Я тебе не зрозумів, спробуй ще раз")

    # await message.answer(message.text)
    # await message.reply(message.text+ str(message.from_user.id))
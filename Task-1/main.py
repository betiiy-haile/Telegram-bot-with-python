import os
from dotenv import load_dotenv

from aiogram import types, Bot, Dispatcher
from aiogram import executor

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


# start command 
@dp.message_handler(commands=['start'])
async def cmd_start(msg: types.Message):
    user = msg.from_user
    if user.first_name:
        start_text = f'Hello, {user.first_name}!👋 Welcome to this Bot.'
    else:
        start_text = 'Hello! 👋 Welcome to out Bot'
    await msg.answer(start_text)

# help command 
@dp.message_handler(commands=['help'])
async def cmd_help(msg: types.Message):
    help_text = """
    <b>Bot Help</b>
    
    <b>Available commands:</b>
    /help - Show this help message.
    /start - Start the bot.
    /hello_world - Get hello world message.
    
    <b>Usage:</b>
    - Send /help to display this help message.
    - Send /start to start the bot.
    - Send /hello_world to see hello world message.

    """
    await msg.answer(help_text)

# hello_world command
@dp.message_handler(commands=['hello_world'])
async def cmd_hello(msg: types.Message):

    reply_text = 'Hello world'
    await msg.answer(reply_text)


if __name__ == "__main__":
    executor.start_polling(dp) 
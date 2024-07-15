"""
This is an echo bot.
It echoes any incoming text messages.
"""

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API token from environment variables
API_TOKEN = os.getenv("TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Handler for /start and /help commands
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when the user sends `/start` or `/help` command.
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

# Echo handler for all messages
@dp.message_handler()
async def echo(message: types.Message):
    """
    This handler will be called for any message that is not a command.
    It echoes the message back to the sender.
    """
    await message.answer(message.text)

# Start polling
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

from aiogram import Bot, Dispatcher, executor, types
import time
import asyncio

API_TOKEN = ''

# Configure logging


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)

async def mei():
    await bot.unban_chat_member(chat_id=-1001459820272, user_id=389319816)


asyncio.run(mei())

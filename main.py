from aiogram import Bot, Dispatcher, executor, types
import time

API_TOKEN = '1939859866:AAEcckHkODkDwIPVjQfUouXcv_sP85xiCQU'

# Configure logging


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['mmm'], is_chat_admin=-1001459820272, user_id = [383387282, 385864579, 352220645])
async def send_welcome(message: types.Message):
    if ' ' in message.text:
        print(' no ')
        mute_time = int(message.text.split(' ')[1])
        print(mute_time)
    else:
        mute_time = 1/12
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    who = message["reply_to_message"]["from"]["id"]
    chat_id = message["chat"]["id"]
    #await message.answer(f'Всем привет, кроме кое-кого. Ему не привет на еще {round(mute_time)*60*60} секуууууунд')
    print(f'muted for {round(mute_time * 60 * 60)}')
    await bot.send_message(chat_id=chat_id, text=f'=0')
    await bot.restrict_chat_member(chat_id=-1001459820272, user_id = who, until_date=time.time()+round(mute_time * 60 * 60))
    print(f'muted for {round(mute_time)*60*60}')


@dp.message_handler(text_contains=['zapravka'], is_chat_admin=-1001459820272)
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    await message.delete()
    try:
        await bot.restrict_chat_member(chat_id=-1001459820272, user_id=user_id,
                                    until_date=time.time() + round(9999 * 60 * 60))
    except:
        await message.answer('Свой среди чужих бля пидораааас')



if __name__ == '__main__':
    executor.start_polling(dp)
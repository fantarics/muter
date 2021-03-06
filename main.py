from aiogram import Bot, Dispatcher, executor, types
import time

API_TOKEN = 'token'
CHAT_ID = 'chat_id'
ADMINS = []
BANNED_WORDS = ['zapravka']
# Configure logging
API_TOKEN = input('api_token')
CHAT_ID = input('what is the chat_id')
answer = input('admin user_id')
while int(answer) != 0:
    ADMINS.append(answer)
    answer = input('admin user_id. 0 on finish')

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['add_kw'], is_chat_admin=CHAT_ID, user_id = 383387282)
async def add_moder(message: types.Message):
    if ' ' in message.text:
        new_word = message.text.split(' ')[1]
        BANNED_WORDS.append(new_word)
        await message.answer(text = f'{BANNED_WORDS}')
        
@dp.message_handler(commands=['add_mod'], is_chat_admin=CHAT_ID, user_id = 383387282)
async def add_moder(message: types.Message):
    if ' ' in message.text:
        new_moder = message.text.split(' ')[1]
        ADMINS.append(new_moder)
        await message.answer(text = f'{ADMINS}')
        
@dp.message_handler(commands=['mmm'], is_chat_admin=CHAT_ID, user_id = ADMINS)
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
    await bot.restrict_chat_member(chat_id=chat_id, user_id = who, until_date=time.time()+round(mute_time * 60 * 60))
    print(f'muted for {round(mute_time)*60*60}')


@dp.message_handler(text_contains='_bot', chat_id=CHAT_ID)
@dp.message_handler(text_contains='zapravka', chat_id=CHAT_ID)
@dp.message_handler(text_contains='auto', chat_id=CHAT_ID)
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    await message.delete()
    try:
        await bot.restrict_chat_member(chat_id=CHAT_ID, user_id=user_id,
                                    until_date=time.time() + round(9999 * 60 * 60))
    except:
        await message.answer('Свой среди чужих..................')



if __name__ == '__main__':
    executor.start_polling(dp)

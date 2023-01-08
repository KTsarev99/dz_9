from create_bot import dp
from aiogram import executor
import handlers

async def onStart(_):
    print('Бот запущен!')
    
handlers.registred_handlers(dp)


executor.start_polling(dp, skip_updates=True, on_startup=onStart)
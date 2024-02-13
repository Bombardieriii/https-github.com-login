from aiogram import Bot, Dispatcher

import asyncio

from aiogram.types import AllowedUpdates

bot = Bot(token='6402117547:AAE8EIVJvEfGs77cxek1W9exwXvjPDjyvc4')
dp = Dispatcher(bot=bot)

async def main():
    from handlers import dp
    try:
        await dp.start_polling(bot, allowed_updates=AllowedUpdates.all())
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')
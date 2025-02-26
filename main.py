import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.exceptions import TelegramBadRequest

movies = {
    '123': {
        'poster': 'Slova patsana',
        'title': 'silovo patasas'
    }
}

TOKEN = "8101475312:AAFJt-Ys47EZ29cbMW8C8_NGrODjleafbuo"
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
CHANELL_ID = "@dilmurod_leetcode"

async def is_subscribed(user_id: int) -> bool:
    try:
        number = await bot.get_chat_member(chat_id=CHANELL_ID, user_id=user_id)
        return number.status in ['member', 'administrator', 'creator']
    except TelegramBadRequest:
        return False

@dp.message(Command('start'))
async def catch_start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Code & Coffee', url='https://t.me/dilmurod_leetcode')],
            [InlineKeyboardButton(text='Tekshirish', callback_data='check_subscribe')]
        ]
    )
    await message.answer(text="Botdan foydalanish uchun kanalaga azo bo'ling", reply_markup=keyboard)

@dp.callback_query(F.data == 'check_subscribe')
async def check_is_subscribed(callback_query: CallbackQuery):
    if await is_subscribed(callback_query.from_user.id):
        await callback_query.message.edit_text(text="Assalomu alaykum!\n\nKinoning kodini yuboring, men sizga kinoni topib beraman! 🎬")
    else:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='Code & Coffee', url='https://t.me/dilmurod_leetcode')],
                [InlineKeyboardButton(text='Tekshirish', callback_data='check_subscribe')]
            ]
        )
        await callback_query.answer("❌ Siz hali obuna bo‘lmadingiz! Iltimos, obuna bo‘ling.", show_alert=True)
        await callback_query.message.edit_text(
            text="Bo'tdan to'liq foydalanish uchun kanalga obuna bo'ling!",
            reply_markup=keyboard
        )


@dp.message()
async def send_movie(message: Message):
    code = message.text.strip()
    movie = movies.get(code)
    if movie:
        await message.answer_photo(movie["poster"], caption=movie["title"])
    else:
        await message.answer("Kechirasiz, bunday kodga mos kino topilmadi. ❌")

async def main():
    print('working')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
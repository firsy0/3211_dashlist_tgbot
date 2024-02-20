import asyncio
import logging
import sys
import time
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6499148020:AAHr3gN8wbSRlgpeeK0vDHifM5OVpMQT-40"
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


#### REPLY KEYBOARD MARKUP
def r_main_menu():
    main_menu = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Verified List"), KeyboardButton(text="Silent List"), KeyboardButton(text="Challenge List")
        ], [
            KeyboardButton(text="Settings ⚙️"), KeyboardButton(text="About Us")
    ]],
    resize_keyboard=True
    )
    return main_menu

def r_settings():
    settings = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Language 🇬🇧"), KeyboardButton(text="Stroke value 📄")
        ], [
            KeyboardButton(text="Go back")
        ]],
    resize_keyboard=True
    )
    return settings

def r_vl():
    vl = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Show on site", url='https://firsy0.github.io/3211-dashlist/vl.html'), InlineKeyboardButton(text="Show in bot", callback_data="vlbot")
    ]])
    return vl

@dp.callback_query(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data
    chat_id = callback_query.from_user.id
    if data == "vlbot":
        media.group = MediaGroupBuilder(caption="Media group caption")
        media.group.add_photo(media="https//picsum.photos/200/300")
        await bot.send_media_group(chat_id=chat_id, media=media.group.build())

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", reply_markup=r_main_menu())

@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
        print("___flag", message.text)
        if message.text == "Settings ⚙️":
            await message.answer("You are in the settings", reply_markup=r_settings())
        elif message.text == "Go back":
            await message.answer("You are in the main menu", reply_markup=r_main_menu())
        elif message.text == "Verified List":
            await message.answer("❔ What is Verified list?\n\nVerified list shows the 20 hardest levels over 1 minute that are rated or can be rated by RobTop. \n\n❔ Why is this list needed?\n\nThe current highest difficulty rating (Extreme Demon) is not enough, because the skill of the players has gone beyond this difficulty. That's why this list is needed so that players understand which levels are in the 20 most difficult and can compare them.\n\n❔ How did you determine the positions of the levels in the list?\n\nThe position of a level in the list is affected by its length and complexity.", reply_markup=r_vl())

    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

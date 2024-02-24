import asyncio
import logging
import sys
import time
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold, hlink
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6499148020:AAHr3gN8wbSRlgpeeK0vDHifM5OVpMQT-40"

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
def r_main_menu():
    main_menu = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="News"), KeyboardButton(text="Lists")
        ], [
            KeyboardButton(text="About Us")
    ]],
    resize_keyboard=True
    )
    return main_menu

def r_lists():
    lists = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Verified List"), KeyboardButton(text="Silent List"), KeyboardButton(text="Challenge List")
        ], [
            KeyboardButton(text="Go back")
        ]],
    resize_keyboard=True
    )
    return lists

def r_aboutus():
    about_us = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="GitHub🌐"), KeyboardButton(text="Telegram🌐"), KeyboardButton(text="Discord🌐")
        ], [
            KeyboardButton(text="Go back")
        ]],
    resize_keyboard=True
    )
    return about_us
def r_vlist():
    vlist = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Show VL on site", url='https://firsy0.github.io/3211-dashlist/vl.html'), InlineKeyboardButton(text="Show VL in bot", callback_data="vlist_show")
        ]],
    resize_keyboard=True
    )
    return vlist

@dp.callback_query(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data
    chat_id = callback_query.from_user.id
    if data == "vlist_show":
        
        print("VList were successfully showed to", chat_id)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", reply_markup=r_main_menu())

@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
        if message.text == "Lists":
            time.sleep(0.3)
            await message.answer("There is 3 lists in this bot:\n\nVerified list\n\nSilent list\n\nChallenge list\n")
            time.sleep(0.3)
            await message.answer("Which one you want to open?", reply_markup=r_lists())

        elif message.text == "Verified List":
            await message.answer("❔ What is Verified list?\n\nVerified list shows the 20 hardest levels over 1 minute that are rated or can be rated by RobTop. \n\n❔ Why is this list needed?\n\nThe current highest difficulty rating (Extreme Demon) is not enough, because the skill of the players has gone beyond this difficulty. That's why this list is needed so that players understand which levels are in the 20 most difficult and can compare them.\n\n❔ How did you determine the positions of the levels in the list?\n\nThe position of a level in the list is affected by its length and complexity.", reply_markup=r_vlist())
        elif message.text == "Show VL in bot":
            await message.answer("1")

        elif message.text == "News":
            await message.answer("You are in the settings", reply_markup=r_lists())

        elif message.text == "About Us":
            await message.answer("If you want to contact me", reply_markup=r_aboutus())

        elif message.text == "GitHub🌐":
            await message.answer(f"GitHub links:\n\n{hlink('Profile🐍', 'https://github.com/firsy0')}\n{hlink('Repository🐍', 'https://github.com/firsy0/3211-dashlist')}")
        elif message.text == "Telegram🌐":
            await message.answer("Telegram:\n\n@firsy0")
        elif message.text == "Go back":
            await message.answer("You are in the main menu", reply_markup=r_main_menu())

    except TypeError:
        print("Error")
async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

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
            KeyboardButton(text="🗞 News"), KeyboardButton(text="📋 Lists")
        ], [
            KeyboardButton(text="🌐 Contact")
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



newsList = ["Tidal Wave got rated!",
            "2.2 update release",
            "Tidal Wave is verified",
            "❌",
            "❌",
            "❌"]

def r_news():
    news = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="1️⃣ - " + newsList[0]), KeyboardButton(text="2️⃣ - " + newsList[1]), KeyboardButton(text="3️⃣ - " + newsList[2]),
        ], [
            KeyboardButton(text="4️⃣ - " + newsList[3]), KeyboardButton(text="5️⃣ - " + newsList[4]), KeyboardButton(text="6️⃣ - " + newsList[5]),
        ], [
            KeyboardButton(text="Go back")
        ]],
        resize_keyboard=True
    )
    return news

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
        await bot.send_message(chat_id,"Showing Verified List...")
        print("|✅| VList ->", chat_id)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", reply_markup=r_main_menu())

@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
        if message.text == "📋 Lists":
            time.sleep(0.3)
            await message.answer(f"{hbold('Lists')}")
            await message.answer("🔎There are 3 lists in this bot:\n\n📋 Verified list\n\n📋 Silent list\n\n📋 Challenge list\n")
            time.sleep(0.3)
            await message.answer("Which one are you want to open?", reply_markup=r_lists())

        elif message.text == "Verified List":
            await message.answer(f"{hbold('Verified List')}""❔ What is Verified list?\n\nVerified list shows the 20 hardest levels over 1 minute that are rated or can be rated by RobTop. \n\n❔ Why is this list needed?\n\nThe current highest difficulty rating (Extreme Demon) is not enough, because the skill of the players has gone beyond this difficulty. That's why this list is needed so that players understand which levels are in the 20 most difficult and can compare them.\n\n❔ How did you determine the positions of the levels in the list?\n\nThe position of a level in the list is affected by its length and complexity.", reply_markup=r_vlist())

        elif message.text == "🗞 News":
            await message.answer("📰 Showing last 6 posts..", reply_markup=r_news())
                    # Posts #
        # 1
        elif newsList[0] in message.text:
            await message.answer("1")
        # 2
        elif newsList[1] in message.text:
            await message.answer("1")
        # 3
        elif newsList[2] in message.text:
            await message.answer("1")
        # 4
        elif newsList[3] in message.text:
            await message.answer("There is no post")
        # 5
        elif newsList[4] in message.text:
            await message.answer("There is no post")
        # 6
        elif newsList[5] in message.text:
            await message.answer("There is no post")

        elif message.text == "🌐 Contact":
            await message.answer("💬You can contact the author of the bot in these ways:\n\n" f"{hlink('🔗Telegram', 'https://t.me/firsy0')}\n" "💬Discord (firsy#8192)\n" f"{hlink('🔗GitHub', 'https://github.com/firsy0')}")

        elif message.text == "Go back":
            await message.answer("⬅️ You are in the main menu", reply_markup=r_main_menu())

        elif message.text == "1488":
            await message.answer("Ооооо, ето ше пасхалкооо😁😁😁😁😁😁😏😏😏😏😏😏😏")
            await message.answer("Включаите вентилятари!😏😏😏😏😏😏😏😏")
            print("Омагад ", message.from_user.full_name, " нашол пасхалкоооооооо!!!!")

    except TypeError:
        print("Error")
async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

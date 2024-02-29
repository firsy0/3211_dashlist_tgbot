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



vl_name = ["Level Name",
           "Tidal Wave",
           "Acheron",
           "Avernus",
           "Silent Clubstep",
           "Abyss of Darkness",
           "Kyouki",
           "Sakupen Circles",
           "Slaughterhouse",
           "Firework",
           "ETERNALtheory",
           "KOCMOC",
           "Deimos",
           "COMBUSTION",
           "MINUSdry",
           "The Lightning Rod",
           "Through The Gates",
           "POOCUBED",
           "Stellar Night",
           "Eyes in the Water",
           "LIMBO"]

vl_host = ["Hosted by",
           "OniLink",
           "ryamu",
           "PockeWildfish",
           "TheRealSailent",
           "Exen",
           "Demishio",
           "DrCuber",
           "icedcave",
           "Vernam",
           "Hyperlith",
           "Vernam",
           "ItsHybrid",
           "Cersia",
           "CDMusic",
           "Lavatrex",
           "TeamTheDashers",
           "btLisp",
           "icedcave",
           "hawkyre",
           "MindCap"]

vl_verify = ["Verified by",
           "Zoink",
           "Zoink",
           "Zoink",
           "zoe",
           "Cursed",
           "Demishio",
           "Diamond",
           "Doggie",
           "Trick",
           "Hyperlith",
           "Zoink",
           "Doggie",
           "Slithium",
           "Varium",
           "Lavatrex",
           "Exen",
           "Kyasshukodo",
           "Tuggy",
           "LordVadercraft",
           "BUNNYGRAM"]

vl_id = ["In-game ID",
           "86407629",
           "73667628",
           "89496627",
           "4125776",
           "49896559",
           "86018142",
           "76962930",
           "27690100",
           "75206202",
           "92196326",
           "87665224",
           "93091893",
           "94359172",
           "89414220",
           "93917076",
           "49072489",
           "85133223",
           "83244159",
           "95851008",
           "86084399"]

def r_vlist_sc():
    vlist_sc = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Show VL on site", url='https://firsy0.github.io/3211-dashlist/vl.html'), InlineKeyboardButton(text="Show VL in bot", callback_data="vlist_sc")
        ]],
    resize_keyboard=True
    )
    return vlist_sc

def r_vlist1_5():
    vlist1_5 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="1. " + vl_name[1], callback_data="vl1")],[
            InlineKeyboardButton(text="2. " + vl_name[2], callback_data="vl2")],[
            InlineKeyboardButton(text="3. " + vl_name[3], callback_data="vl3")],[
            InlineKeyboardButton(text="4. " + vl_name[4], callback_data="vl4")],[
            InlineKeyboardButton(text="5. " + vl_name[5], callback_data="vl5")],[
            InlineKeyboardButton(text="▶️", callback_data="vlgoto6_10")]
        ],
    resize_keyboard=True
    )
    return vlist1_5

def r_vlist6_10():
    vlist6_10 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="6. " + vl_name[6], callback_data="vl6")],[
            InlineKeyboardButton(text="7. " + vl_name[7], callback_data="vl7")],[
            InlineKeyboardButton(text="8. " + vl_name[8], callback_data="vl8")],[
            InlineKeyboardButton(text="9. " + vl_name[9], callback_data="vl9")],[
            InlineKeyboardButton(text="10. " + vl_name[10], callback_data="vl10")],[
            InlineKeyboardButton(text="◀️", callback_data="vlgoto1_5"), InlineKeyboardButton(text="▶️", callback_data="vlgoto11_15")]
        ],
    resize_keyboard=True
    )
    return vlist6_10

def r_vlist11_15():
    vlist11_15 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="11. " + vl_name[11], callback_data="vl11")],[
            InlineKeyboardButton(text="12. " + vl_name[12], callback_data="vl12")],[
            InlineKeyboardButton(text="13. " + vl_name[13], callback_data="vl13")],[
            InlineKeyboardButton(text="14. " + vl_name[14], callback_data="vl14")],[
            InlineKeyboardButton(text="15. " + vl_name[15], callback_data="vl15")],[
            InlineKeyboardButton(text="◀️", callback_data="vlgoto6_10"), InlineKeyboardButton(text="▶️", callback_data="vlgoto16_20")]
        ],
    resize_keyboard=True
    )
    return vlist11_15

def r_vlist16_20():
    vlist16_20 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="16. " + vl_name[16], callback_data="vl16")],[
            InlineKeyboardButton(text="17. " + vl_name[17], callback_data="vl17")],[
            InlineKeyboardButton(text="18. " + vl_name[18], callback_data="vl18")],[
            InlineKeyboardButton(text="19. " + vl_name[19], callback_data="vl19")],[
            InlineKeyboardButton(text="20. " + vl_name[20], callback_data="vl20")],[
            InlineKeyboardButton(text="◀️", callback_data="vlgoto11_15")]
        ],
    resize_keyboard=True
    )
    return vlist16_20

@dp.callback_query(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data
    chat_id = callback_query.from_user.id
    if data == "vlist_sc":
        await bot.send_message(chat_id,"Showing Verified List...")
        await bot.send_message(chat_id,"Verified List (1 to 5 of 20)", reply_markup=r_vlist1_5())
        print("|✅| VList ->", chat_id)

    elif data == "vlgoto1_5":
        await bot.send_message(chat_id,"Verified List (1 to 5 of 20)", reply_markup=r_vlist1_5())
    elif data == "vlgoto6_10":
        await bot.send_message(chat_id, "Verified List (6 to 10 of 20)", reply_markup=r_vlist6_10())
    elif data == "vlgoto11_15":
        await bot.send_message(chat_id, "Verified List (11 to 15 of 20)", reply_markup=r_vlist11_15())
    elif data == "vlgoto16_20":
        await bot.send_message(chat_id, "Verified List (16 to 20 of 20)", reply_markup=r_vlist16_20())

    elif data == "vl1":
        await bot.send_message(chat_id, "1. " + vl_name[1] + "\n\nInformation about level: \n\nHosted by: " + vl_host[1] + "\nVerified by: " + vl_verify[1] + "\nIn-game ID: " + vl_id[1])
    elif data == "vl2":
        await bot.send_message(chat_id, "2. " + vl_name[2] + "\n\nInformation about level: \n\nHosted by: " + vl_host[2] + "\nVerified by: " + vl_verify[2] + "\nIn-game ID: " + vl_id[2])
    elif data == "vl3":
        await bot.send_message(chat_id, "3. " + vl_name[3] + "\n\nInformation about level: \n\nHosted by: " + vl_host[3] + "\nVerified by: " + vl_verify[3] + "\nIn-game ID: " + vl_id[3])
    elif data == "vl4":
        await bot.send_message(chat_id, "4. " + vl_name[4] + "\n\nInformation about level: \n\nHosted by: " + vl_host[4] + "\nVerified by: " + vl_verify[4] + "\nIn-game ID: " + vl_id[4])
    elif data == "vl5":
        await bot.send_message(chat_id, "5. " + vl_name[5] + "\n\nInformation about level: \n\nHosted by: " + vl_host[5] + "\nVerified by: " + vl_verify[2] + "\nIn-game ID: " + vl_id[5])
    elif data == "vl6":
        await bot.send_message(chat_id, "6. " + vl_name[6] + "\n\nInformation about level: \n\nHosted by: " + vl_host[6] + "\nVerified by: " + vl_verify[1] + "\nIn-game ID: " + vl_id[6])
    elif data == "vl7":
        await bot.send_message(chat_id, "7. " + vl_name[7] + "\n\nInformation about level: \n\nHosted by: " + vl_host[7] + "\nVerified by: " + vl_verify[2] + "\nIn-game ID: " + vl_id[7])
    elif data == "vl8":
        await bot.send_message(chat_id, "8. " + vl_name[8] + "\n\nInformation about level: \n\nHosted by: " + vl_host[8] + "\nVerified by: " + vl_verify[3] + "\nIn-game ID: " + vl_id[8])
    elif data == "vl9":
        await bot.send_message(chat_id, "9. " + vl_name[9] + "\n\nInformation about level: \n\nHosted by: " + vl_host[9] + "\nVerified by: " + vl_verify[1] + "\nIn-game ID: " + vl_id[9])
    elif data == "vl10":
        await bot.send_message(chat_id, "10. " + vl_name[10] + "\n\nInformation about level: \n\nHosted by: " + vl_host[10] + "\nVerified by: " + vl_verify[10] + "\nIn-game ID: " + vl_id[10])
    elif data == "vl11":
        await bot.send_message(chat_id, "11. " + vl_name[11] + "\n\nInformation about level: \n\nHosted by: " + vl_host[11] + "\nVerified by: " + vl_verify[11] + "\nIn-game ID: " + vl_id[11])
    elif data == "vl12":
        await bot.send_message(chat_id, "12. " + vl_name[12] + "\n\nInformation about level: \n\nHosted by: " + vl_host[12] + "\nVerified by: " + vl_verify[12] + "\nIn-game ID: " + vl_id[12])
    elif data == "vl13":
        await bot.send_message(chat_id, "13. " + vl_name[13] + "\n\nInformation about level: \n\nHosted by: " + vl_host[13] + "\nVerified by: " + vl_verify[13] + "\nIn-game ID: " + vl_id[13])
    elif data == "vl14":
        await bot.send_message(chat_id, "14. " + vl_name[14] + "\n\nInformation about level: \n\nHosted by: " + vl_host[14] + "\nVerified by: " + vl_verify[14] + "\nIn-game ID: " + vl_id[14])
    elif data == "vl15":
        await bot.send_message(chat_id, "15. " + vl_name[15] + "\n\nInformation about level: \n\nHosted by: " + vl_host[15] + "\nVerified by: " + vl_verify[15] + "\nIn-game ID: " + vl_id[15])
    elif data == "vl16":
        await bot.send_message(chat_id, "16. " + vl_name[16] + "\n\nInformation about level: \n\nHosted by: " + vl_host[16] + "\nVerified by: " + vl_verify[16] + "\nIn-game ID: " + vl_id[16])
    elif data == "vl17":
        await bot.send_message(chat_id, "17. " + vl_name[17] + "\n\nInformation about level: \n\nHosted by: " + vl_host[17] + "\nVerified by: " + vl_verify[17] + "\nIn-game ID: " + vl_id[17])
    elif data == "vl18":
        await bot.send_message(chat_id, "18. " + vl_name[18] + "\n\nInformation about level: \n\nHosted by: " + vl_host[18] + "\nVerified by: " + vl_verify[18] + "\nIn-game ID: " + vl_id[18])
    elif data == "vl19":
        await bot.send_message(chat_id, "19. " + vl_name[19] + "\n\nInformation about level: \n\nHosted by: " + vl_host[19] + "\nVerified by: " + vl_verify[19] + "\nIn-game ID: " + vl_id[19])
    elif data == "vl20":
        await bot.send_message(chat_id, "20. " + vl_name[20] + "\n\nInformation about level: \n\nHosted by: " + vl_host[20] + "\nVerified by: " + vl_verify[20] + "\nIn-game ID: " + vl_id[20])

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
            await message.answer("🔎There are 3 lists in this bot:\n\n📋✅ Verified list\n\n📋⏳ Silent list\n\n📋⏳ Challenge list\n")
            time.sleep(0.3)
            await message.answer("Which one are you want to open?", reply_markup=r_lists())

        elif message.text == "Verified List":
            await message.answer(f"{hbold('Verified List')}\n\n""❔ What is Verified list?\n\nVerified list shows the 20 hardest levels over 1 minute that are rated or can be rated by RobTop. \n\n❔ Why is this list needed?\n\nThe current highest difficulty rating (Extreme Demon) is not enough, because the skill of the players has gone beyond this difficulty. That's why this list is needed so that players understand which levels are in the 20 most difficult and can compare them.\n\n❔ How did you determine the positions of the levels in the list?\n\nThe position of a level in the list is affected by its length and complexity.", reply_markup=r_vlist_sc())

        elif message.text == "🗞 News":
            await message.answer("📰 Showing last 6 posts..", reply_markup=r_news())
                    # Posts #
        # 1
        elif newsList[0] in message.text:
            await message.answer("Finally, RobTop saw Tidal Wave and gave him rate.")
        # 2
        elif newsList[1] in message.text:
            await message.answer("After more than 5 years 2.2 update is released.")
        # 3
        elif newsList[2] in message.text:
            await message.answer("Zoink verified Tidal Wave, he spent about 50000 attempts to beat it.")
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


    except TypeError:
        print("Error")
async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

from pyrogram import filters
from pyrogram import __version__ as pyro_vr
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from .. import (Venom1, Venom2, Venom3, Venom4,
                Venom5, Venom6, Venom7, Venom8,
                Venom9, Venom10, Venom11, Venom12,
                Venom13, Venom14, Venom15, HNDLR,
                SUDO_USERS, vcbot, ALIVE_PIC, __version__)                   

Array = ALIVE_PIC or "https://telegra.ph/file/7c38bf5378fa5c7eba601.jpg"

 
@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
async def _Alive(_, e: Message):
    ids = 0
    try:
        if Venom1:
            ids += 1
        if Venom2:
            ids += 1
        if Venom3:
            ids += 1
        if Venom4:
            ids += 1
        if Venom5:
            ids += 1
        if Venom6:
            ids += 1
        if Venom7:
            ids += 1
        if Venom8:
            ids += 1
        if Venom9:
            ids += 1
        if Venom10:
            ids += 1
        if Venom11:
            ids += 1
        if Venom12:
            ids += 1
        if Venom13:
            ids += 1
        if Venom14:
            ids += 1
        if Venom15:
            ids += 1
        Array_msg = f"â¢ðð¥ð¢ð§ððð¥ð¦ ð©ð ð¢ð¡ððð¡ðâ¢. ð¥ \n\n"
        Array_msg += f"â ââââââ â ââââââ â \n"
        Array_msg += f"âº Êá´á´ á´ á´ÊsÉªá´É´ : `{__version__}` \n"
        Array_msg += f"âº á´ÊÊá´ á´ á´ÊsÉªá´É´ : `{pyro_vr}` \n"
        Array_msg += f"âº Aá´á´Éªá´ á´ IDs : `{ids}` \n"
        Array_msg += f"âº Sá´á´á´á´Êá´ : [Já´ÉªÉ´.](https://t.me/The_Brothers_Group) \n"
        Array_msg += f"â ââââââ â ââââââ â \n\n"
        await e.reply_photo(
        photo=Array,
        caption=Array_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "â¢ Channel â¢", url="https://t.me/NISHU_BOTHUB")
                ], [
                    InlineKeyboardButton(
                        "â¢ Sá´á´á´á´Êá´ â¢", url="https://t.me/shivamdemon")
                ]],
        ),
    ) 
    except Exception as lol:         
        Array_msg = f"â¢ðð¥ð¢ð§ððð¥ð¦ ð©ð ð¢ð¡ððð¡ðâ¢. ð¥ \n\n"
        Array_msg += f"â ââââââ â ââââââ â \n"
        Array_msg += f"âº Êá´á´ á´ á´ÊsÉªá´É´ : `{__version__}` \n"
        Array_msg += f"âº á´ÊÊá´ á´ á´ÊsÉªá´É´ : `{pyro_vr}` \n"
        Array_msg += f"âº Sá´á´á´á´Êá´ : [Já´ÉªÉ´.](https://t.me/The_Brothers_Group) \n"
        Array_msg += f"â ââââââ â ââââââ â \n\n"
        await e.reply_photo(
        photo=Array,
        caption=Array_msg,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("â¢ Channel â¢", url="https://t.me/NISHU_BOTHUB"),
                ],
                [
                    InlineKeyboardButton("â¢ Sá´á´á´á´Êá´ â¢", url="https://t.me/shivamdemon"),
                ],
            ],
        ),
    ) 

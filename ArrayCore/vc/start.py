#@TheVenomXD

from pyrogram import Client, filters
from pyrogram.types import Message

from ..utils import vcbot, SUDO_USERS, HNDLR, hl, START_VID

# @vcbot.on_message(filters.user(SUDO_USERS) & filters.private & filters.command(["start"], prefixes=HNDLR))
# async def start(_, e: Message):
   # video=START_VID,
  # await vcbot.send_video(e.chat.id, video, f"Vc Raid Bot Is Working Fine. \nSend `{hl}help` To Know Your Commands. \n\n< Powered By @ArrayCore >")


@vcbot.on_message(command(["start"]))
async def _start(_, ok: Message):
    if ok.chat.type == "private":
        await ok.reply_text(
            f"**Hello {Message.from_user.mention} !** \n\n __ • I'm ArrayCore An Advance And Simple Group Voice Call Bot__ \n\n **Click Below Buttons for More Info**",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• Channel •", url="https://t.me/ArrayCore"),
                    InlineKeyboardButton(
                        "• Support •", url="https://t.me/DNHxHELL")
                ], [
                    InlineKeyboardButton(
                        "• Repo •", url="https://github.com/desinobita/TgVcUsers")
                ]]
            ))
    else:
        await ok.reply_text("**✨ ArrayCore is On ✨**",
                           reply_markup=InlineKeyboardMarkup(
                               [[
                                   InlineKeyboardButton("• Channel •", url="https://t.me/ArrayCore")
                               ]]
                           )
                           )

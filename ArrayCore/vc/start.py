#@TheVenomXD

from pyrogram import Client, filters
from pyrogram.types import Message

from ..utils import vcbot, SUDO_USERS, HNDLR, hl, START_VID

@vcbot.on_message(filters.user(SUDO_USERS) & filters.private & filters.command(["start"], prefixes=HNDLR))
async def start(_, e: Message):
    video=START_VID,
    await vcbot.send_video(e.chat.id, video, f"Vc Raid Bot Is Working Fine. \nSend `{hl}help` To Know Your Commands. \n\n< Powered By @ArrayCore >")

import os
import sys

from pyrogram import filters
from pyrogram.types import Message

from search import (Venom1, Venom2, Venom3, Venom4,
                    Venom5, Venom6, Venom7, Venom8,
                    Venom9, Venom10, Venom11, Venom12,
                    Venom13, Venom14, Venom15, vcbot,
                    HNDLR, call_py, contact_filter, SUDO_USERS)
    

@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=HNDLR))
async def ping(_, e: Message):
    await e.reply_text("`Restarting...`")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()

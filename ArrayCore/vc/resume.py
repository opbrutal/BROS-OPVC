from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from config import bot, call_py, HNDLR, contact_filter
from ArrayCore.vc.handlers import skip_current_song, skip_item
from ArrayCore.vc.queues import QUEUE, clear_queue
from var import Var
from search import (Venom1, Venom2, Venom3, Venom4,
                    Venom5, Venom6, Venom7, Venom8,
                    Venom9, Venom10, Venom11, Venom12,
                    Venom13, Venom14, Venom15, vcbot,
                    HNDLR, call_py, contact_filter, SUDO_USERS)

SUDO_USERS = []
for x in Var.SUDO_USERS: 
    SUDO_USERS.append(x)

@vcbot.on_message(filters.user(SUDO_USERS) & filters.private & filters.command(["resume"], prefixes=HNDLR))
async def ping(_, e: Message):
    if e.from_user.id in SUDO_USERS:
        await e.delete()
        chat_id = e.chat.id
        if chat_id in QUEUE:
            try:
                await call_py.resume_stream(chat_id)
                await e.reply(
                    f"**Resumed In {chat_id}**"
                )
            except Exception as e:
                await e.reply(f"**ERROR** \n`{e}`")
    else:
        await e.reply("**Nothing is currently paused!**")

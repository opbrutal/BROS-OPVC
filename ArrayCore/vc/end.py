import os

from pyrogram import Client, filters
from pyrogram.types import Message

from ArrayCore.vc.handlers import skip_current_song, skip_item
from ArrayCore.vc.queues import clear_queue, QUEUE
from search import (Venom1, Venom2, Venom3, Venom4,
                    Venom5, Venom6, Venom7, Venom8,
                    Venom9, Venom10, Venom11, Venom12,
                    Venom13, Venom14, Venom15, vcbot,
                    HNDLR, contact_filter, SUDO_USERS)
from search import (call_py1, call_py2, call_py3, call_py4,
               call_py5, call_py6, call_py7, call_py8,
               call_py9, call_py10, call_py11, call_py12,
               call_py13, call_py14, call_py15)



@vcbot.on_message(filters.user(SUDO_USERS) & ~filters.private & filters.command(["end"], prefixes=HNDLR))
async def ping(_, e: Message):
    chat_id = e.chat.id
    if chat_id in QUEUE:
        try:
            await call_py1.leave_group_call(chat_id)
            clear_queue(chat_id)
            await e.reply_text("**End**")
        except Exception as ex:
            await e.reply_text(f"**ERROR** \n`{ex}`")
    else:
        await e.reply_text("**Nothing is playing !**")

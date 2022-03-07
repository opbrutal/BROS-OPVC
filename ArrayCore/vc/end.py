import os

from pyrogram import Client, filters
from pyrogram.types import Message

from ArrayCore.vc.handlers import skip_current_song, skip_item
from ArrayCore.vc.queues import clear_queue, QUEUE
from search import (Venom1, Venom2, Venom3, Venom4,
                    Venom5, Venom6, Venom7, Venom8,
                    Venom9, Venom10, Venom11, Venom12,
                    Venom13, Venom14, Venom15, HNDLR,
                    vcbot, call_py, contact_filter, SUDO_USERS)



@Venom1.on(filters.command(["end"], prefixes=f"{HNDLR}"))
@Venom2.on(filters.command(["end"], prefixes=f"{HNDLR}"))
@Venom3.on(filters.command(["end"], prefixes=f"{HNDLR}"))
@Venom4.on(filters.command(["end"], prefixes=f"{HNDLR}"))
@Venom5.on(filters.command(["end"], prefixes=f"{HNDLR}"))
@Venom6.on(filters.command(["end"], prefixes=f"{HNDLR}"))
@Venom7.on(filters.command(["end"], prefixes=f"{HNDLR}"))
@Venom8.on(filters.command(["end"], prefixes=f"{HNDLR}"))
@Venom9.on(filters.command(["end"], prefixes=f"{HNDLR}"))
@Venom10.on(filters.command(["end"], prefixes=f"{HNDLR}"))
@Venom11.on(filters.command(["end"], prefixes=f"{HNDLR}"))
@Venom12.on(filters.command(["end"], prefixes=f"{HNDLR}"))
@Venom13.on(filters.command(["end"], prefixes=f"{HNDLR}"))
@Venom14.on(filters.command(["end"], prefixes=f"{HNDLR}"))
@Venom15.on(filters.command(["end"], prefixes=f"{HNDLR}"))
async def ping(_, e: Message):
    if e.from_user.id in SUDO_USERS:
        await e.delete()
        chat_id = e.chat.id
        if chat_id in QUEUE:
            try:
                await call_py.leave_group_call(chat_id)
                clear_queue(chat_id)
                await e.reply("**End**")
            except Exception as e:
                await e.reply(f"**ERROR** \n`{e}`")
        else:
            await e.reply("**Nothing is playing !**")

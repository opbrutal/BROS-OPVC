
from pyrogram import filters
from pyrogram.types import Message
from config import bot, call_py, HNDLR, contact_filter
from ArrayCore.vc.handlers import skip_current_song, skip_item
from ArrayCore.vc.queues import QUEUE, clear_queue
from var import Var 
from search.TheVenomXD import Client, Client2, Client3, Client4, Client5, Client6, Client7, Client8, Client9, Client10, Client11, Client12, Client13, Client14, Client15

SUDO_USERS = []
for x in Var.SUDO_USERS: 
    SUDO_USERS.append(x)

@Client.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
@Client2.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
@Client3.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
@Client4.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
@Client5.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
@Client6.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
@Client7.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
@Client8.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
@Client9.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
@Client10.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
@Client11.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
@Client12.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
@Client13.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
@Client14.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
@Client15.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
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




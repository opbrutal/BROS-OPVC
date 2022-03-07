import os
import sys
import asyncio
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from config import bot, call_py, HNDLR, contact_filter
from time import time
from datetime import datetime
from var import Var
from search import Client, Client2, Client3, Client4, Client5, Client6, Client7, Client8, Client9, Client10, Client11, Client12, Client13, Client14, Client15

SUDO_USERS = []
for x in Var.SUDO_USERS: 
    SUDO_USERS.append(x)
    

@vcbot.on_message(filters.user(SUDO_USERS) & filters.private & filters.command(["ping"], prefixes=HNDLR))
async def ping(_, e: Message):
    if e.from_user.id in SUDO_USERS:
        start = time()
        current_time = datetime.utcnow()
        m_reply = await e.reply_text("`Alive♤`")
        delta_ping = time() - start
        uptime_sec = (current_time - START_TIME).total_seconds()
        uptime = await _human_time_duration(int(uptime_sec))
        await m_reply.edit(f"Pong!")

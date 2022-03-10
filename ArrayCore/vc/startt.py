import os
import sys
import asyncio
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from time import time
from datetime import datetime
from search import vcbot 

SUDO_USERS = []
for x in Var.SUDO_USERS: 
    SUDO_USERS.append(x)

@vcbot.on_message(filters.user(SUDO_USERS) & ~filters.private & filters.command(["start"], prefixes=HNDLR))
async def start(_, e: Message):
    if e.from_user.id in SUDO_USERS:
        HELP = f"""
Vc Raid Bot Is Working Fine 
Send !help To Know Your Commands
Powered By @ArrayCore
"""
        await e.reply(HELP)

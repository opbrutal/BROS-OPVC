import os
import sys
import asyncio
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from time import time
from datetime import datetime
from search import vcbot, SUDO_USERS, HNDLR

@vcbot.on_message(filters.user(SUDO_USERS) & ~filters.private & filters.command(["start"], prefixes=HNDLR))
async def start(_, e: Message):
    await client.send_message(
        text = f"""
Vc Raid Bot Is Working Fine 
Send !help To Know Your Commands
Powered By @ArrayCore
"""
        await e.reply(HELP)

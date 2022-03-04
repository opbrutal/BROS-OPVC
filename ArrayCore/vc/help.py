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

SUDO_USERS = []
for x in Var.SUDO_USERS: 
    SUDO_USERS.append(x)

@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def ping(_, e: Message):
    if e.from_user.id in SUDO_USERS:
       HELP = f"""
Help Menu For VcRaid By [Akash](https/t.me/TheVenomXD).
Use Your Command HNDLR To Use It I Am Giving ! As Default

!play - To Play A Audio
!skip - To Skip 
!list - For Queued PlayList
!ping - Check I'm Alive or what
!restart - To Restart The Bot
!help - For Help Menu
!stop - To Stop Playing
"""
       await e.reply(HELP)

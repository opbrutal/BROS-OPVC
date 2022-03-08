import asyncio
import os
import sys

from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message
from time import time

from search import vcbot, HNDLR, SUDO_USERS

HELP = f"""Help Menu For VcRaid By [Akash](https/t.me/TheVenomXD).
Use Your Command HNDLR To Use It I Am Giving ! As Default

`!play` - To Play A Audio
`!skip` - To Skip 
`!list` - For Queued PlayList
`!ping` - Check I'm Alive or what
`!restart` - To Restart The Bot
`!help` - For Help Menu
`!stop` - To Stop Playing
"""

  
@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
async def ping(_, e: Message):
       await e.reply_text(HELP, disable_web_page_preview=True)

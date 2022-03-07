import asyncio
import os
import sys

from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message
from time import time

from search import (Venom1, Venom2, Venom3, Venom4,
                    Venom5, Venom6, Venom7, Venom8,
                    Venom9, Venom10, Venom11, Venom12,
                    Venom13, Venom14, Venom15, HNDLR,
                    call_py, contact_filter, SUDO_USERS)


@Venom1.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
@Venom2.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
@Venom3.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
@Venom4.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
@Venom5.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
@Venom6.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
@Venom7.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
@Venom8.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
@Venom9.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
@Venom10.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
@Venom11.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
@Venom12.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
@Venom13.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
@Venom14.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
@Venom15.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
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

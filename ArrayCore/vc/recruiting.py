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
    
@Client.on_message(filters.command(["restart"], prefixes=f"{HNDLR}"))
@Client2.on_message(filters.command(["restart"], prefixes=f"{HNDLR}"))
@Client3.on_message(filters.command(["restart"], prefixes=f"{HNDLR}"))
@Client4.on_message(filters.command(["restart"], prefixes=f"{HNDLR}"))
@Client5.on_message(filters.command(["restart"], prefixes=f"{HNDLR}"))
@Client6.on_message(filters.command(["restart"], prefixes=f"{HNDLR}"))
@Client7.on_message(filters.command(["restart"], prefixes=f"{HNDLR}"))
@Client8.on_message(filters.command(["restart"], prefixes=f"{HNDLR}"))
@Client9.on_message(filters.command(["restart"], prefixes=f"{HNDLR}"))
@Client10.on_message(filters.command(["restart"], prefixes=f"{HNDLR}"))
@Client11.on_message(filters.command(["restart"], prefixes=f"{HNDLR}"))
@Client12.on_message(filters.command(["restart"], prefixes=f"{HNDLR}"))
@Client13.on_message(filters.command(["restart"], prefixes=f"{HNDLR}"))
@Client14.on_message(filters.command(["restart"], prefixes=f"{HNDLR}"))
@Client15.on_message(filters.command(["restart"], prefixes=f"{HNDLR}"))
async def ping(_, e: Message):
    if e.from_user.id in SUDO_USERS:
       await e.reply("`Restarting...`")
       os.execl(sys.executable, sys.executable, *sys.argv)
   # You probably don't need it but whatever
       quit()

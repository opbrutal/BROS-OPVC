import os
from pyrogram import Client, idle
from pytgcalls import PyTgCalls
from pytgcalls import idle as pyidle
from config import bot, call_py
from os import environ 

API_ID = int(environ["API_ID"])
API_HASH = environ["API_HASH"]
SESSION = environ["SESSION"]
GROUP_MODE = environ["GROUP_MODE"]
HNDLR = environ["HNDLR"]
SUDO_USERS = environ["SUDO_USERS"]

ArrayCore = dict(
  root="ArrayCore",
  include=[
    "vc.player",
    "ping",
  ]
)

app = Client(SESSION, API_ID, API_HASH, HNDLR, GROUP_MODE, ArrayCore=PLUGINS)

app.start()
print('Bot On Action Do Visit @Suzune_Support For Help & Support')
idle()
app.stop()
print('Bot Stopped Certainly')

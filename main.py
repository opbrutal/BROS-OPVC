import os
from pyrogram import Client, idle
from pytgcalls import PyTgCalls
from pytgcalls import idle as pyidle
from config import bot, call_py
from os import environ 

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
session = environ["SESSION"]
group_mode = environ["GROUP_MODE"]
hndlr = environ["HNDLR"]
sudo_users = environ["SUDO_USERS"]

plugins = dict(
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

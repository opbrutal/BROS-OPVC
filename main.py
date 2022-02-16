import os
from pyrogram import Client, idle
from pytgcalls import PyTgCalls
from pytgcalls import idle as pyidle
from config import bot, call_py

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

bot.start()
print("TgVcUsers On Action Do Visit @Suzune_Support")
call_py.start()
print("TgVcUsers Client On Action Do Visit @Suzune_Support")
pyidle()
idle()

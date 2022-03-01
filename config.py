import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from os import getenv

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")
    
# Necessary Vars
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
SESSION = os.getenv("SESSION")
HNDLR = os.getenv("HNDLR", "!")
GROUP_MODE = os.getenv("GROUP_MODE", "True")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "")))
SUDO_HNDLR = os.environ.get("SUDO_HNDLR", r"!")
UB_BLACK_LIST_CHAT = set(int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", ""))
                      
contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)

if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="ArrayCore"))
call_py = PyTgCalls(bot)

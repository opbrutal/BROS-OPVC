import asyncio
import os
import sys
import time

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls


if os.path.exists(".env"):
    load_dotenv(".env")
    
# -------------CONFIGS--------------------
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", None)
SESSION1 = os.getenv("SESSION", None)
SESSION2 = os.getenv("SESSION2", None)
SESSION3 = os.getenv("SESSION3", None)
SESSION4 = os.getenv("SESSION4", None)
SESSION5 = os.getenv("SESSION5", None)
SESSION6 = os.getenv("SESSION6", None)
SESSION7 = os.getenv("SESSION7", None)
SESSION8 = os.getenv("SESSION8", None)
SESSION9 = os.getenv("SESSION9", None)
SESSION10 = os.getenv("SESSION10", None)
SESSION11 = os.getenv("SESSION11", None)
SESSION12 = os.getenv("SESSION12", None)
SESSION13 = os.getenv("SESSION13", None)
SESSION14 = os.getenv("SESSION14", None)
SESSION15 = os.getenv("SESSION15", None)
HNDLR = os.getenv("HNDLR", "!")
GROUP_MODE = os.getenv("GROUP_MODE", "True")
SUDO_USERS = list(filter(lambda x: x, map(int, os.getenv("SUDO_USERS", "1517994352 1789859817 1432756163").split())))
#-----------------------------------------

vcbot = Client("bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)plugins=dict(root="ArrayCore"))
contact_filter = filters.create(lambda _, __, message:(message.from_user and message.from_user.is_contact) or message.outgoing)
start_time = time.time()

if GROUP_MODE == ("True" or "true" or "TRUE"):
    grp = True
else:
    grp = False


#-------------------------CLIENTS-----------------------------
if SESSION1:
    Venom1 = Client(SESSION1, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="ArrayCore.vc"))
    call_py = PyTgCalls(Venom1)

if SESSION2:
    Venom2 = Client(SESSION2, api_id=API_ID, api_hash=API_HASH)
else:
    Venom2 = None

if SESSION3:
    Venom3 = Client(SESSION3, api_id=API_ID, api_hash=API_HASH)
else:
    Venom3 = None

if SESSION4:
    Venom4 = Client(SESSION4, api_id=API_ID, api_hash=API_HASH)
else:
    Venom4 = None

if SESSION5:
    Venom5 = Client(SESSION5, api_id=API_ID, api_hash=API_HASH)
else:
    Venom5 = None

if SESSION6:
    Venom6 = Client(SESSION6, api_id=API_ID, api_hash=API_HASH)
else:
    Venom6 = None
        
if SESSION7:
    Venom7 = Client(SESSION7, api_id=API_ID, api_hash=API_HASH)
else:
    Venom7 = None

if SESSION8:
    Venom8 = Client(SESSION8, api_id=API_ID, api_hash=API_HASH)
else:
    Venom8 = None

if SESSION9:
    Venom9 = Client(SESSION9, api_id=API_ID, api_hash=API_HASH)
else:
    Venom9 = None
    
if SESSION10:
    Venom10 = Client(SESSION10, api_id=API_ID, api_hash=API_HASH)
else:
    Venom10 = None
           
if SESSION11:
    Venom11 = Client(SESSION11, api_id=API_ID, api_hash=API_HASH)
else:
    Venom11 = None

if SESSION12:
    Venom12 = Client(SESSION12, api_id=API_ID, api_hash=API_HASH)
else:
    Venom12 = None

if SESSION13:
    Venom13 = Client(SESSION13, api_id=API_ID, api_hash=API_HASH)
else:
    Venom13 = None

if SESSION14:
    Venom14 = Client(SESSION14, api_id=API_ID, api_hash=API_HASH)
else:
    Venom14 = None

if SESSION15:
    Venom15 = Client(SESSION15, api_id=API_ID, api_hash=API_HASH)
else:
    Venom15 = None
#----------------------------------------------------------------

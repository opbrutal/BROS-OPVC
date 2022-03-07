import os
import asyncio
import sys
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from os import getenv

if os.path.exists(".env"):
    load_dotenv(".env")
    

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")

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
Suar = list(filter(lambda x: x, map(int, getenv("SUDO_USERS", "1517994352 1789859817 1432756163").split())))

contact_filter = filters.create(lambda _, __, message:(message.from_user and message.from_user.is_contact) or message.outgoing)


if GROUP_MODE.lower() == "true"
    grp = True
else:
    grp = False
GRPPLAY = grp


if SESSION1:
    print("Session 1 found")
    Venom1 = Client(SESSION1, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="ArrayCore.vc"))
    call_py = PyTgCalls(Venom1)

if SESSION2:
    print("Session 2 found")
    Venom2 = Client(SESSION2, api_id=API_ID, api_hash=API_HASH)
else:
    Venom2 = None

if SESSION3:
    print("Session 3 found")
    Venom3 = Client(SESSION3, api_id=API_ID, api_hash=API_HASH)
else:
    Venom3 = None

if SESSION4:
    print("Session 4 found")
    Venom4 = Client(SESSION4, api_id=API_ID, api_hash=API_HASH)
else:
    Venom4 = None

if SESSION5:
    print("Session 5 found")
    Venom5 = Client(SESSION5, api_id=API_ID, api_hash=API_HASH)
else:
    Venom5 = None

if SESSION6:
    print("Session 6 found")
    Venom6 = Client(SESSION6, api_id=API_ID, api_hash=API_HASH)
else:
    Venom6 = None
        
if SESSION7:
    print("Session 7 found")
    Venom7 = Client(SESSION7, api_id=API_ID, api_hash=API_HASH)
else:
    Venom7 = None

if SESSION8:
    print("Session 8 found")
    Venom8 = Client(SESSION8, api_id=API_ID, api_hash=API_HASH)
else:
    Venom8 = None

if SESSION9:
    print("Session 9 found")
    Venom9 = Client(SESSION9, api_id=API_ID, api_hash=API_HASH)
else:
    Venom9 = None
    
if SESSION10:
    print("Session 10 found")
    Venom10 = Client(SESSION10, api_id=API_ID, api_hash=API_HASH)
else:
    Venom10 = None
           
if SESSION11:
    print("Session 11 found")
    Venom11 = Client(SESSION11, api_id=API_ID, api_hash=API_HASH)
else:
    Venom11 = None

if SESSION12:
    print("Session 12 found")
    Venom12 = Client(SESSION12, api_id=API_ID, api_hash=API_HASH)
else:
    Venom12 = None

if SESSION13:
    print("Session 13 found")
    Venom13 = Client(SESSION13, api_id=API_ID, api_hash=API_HASH)
else:
    Venom13 = None

if SESSION14:
    print("Session 14 found")
    Venom14 = Client(SESSION14, api_id=API_ID, api_hash=API_HASH)
else:
    Venom14 = None

if SESSION15:
    print("Session 15 found")
    Venom15 = Client(SESSION15, api_id=API_ID, api_hash=API_HASH)
else:
    Venom15 = None
   

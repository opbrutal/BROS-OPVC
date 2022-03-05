
import os
import sys
import random
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
import time
from telethon.tl.functions.messages import ImportChatInviteRequest


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
HNDLR = getenv("HNDLR", default=".")
SESSION = config("SESSION", default=None)
SESSION2 = config("SESSION2", default=None)
SESSION3 = config("SESSION3", default=None)
SESSION4 = config("SESSION4", default=None)
SESSION5 = config("SESSION5", default=None)
SESSION6 = config("SESSION6", default=None)
SESSION7 = config("SESSION7", default=None)
SESSION8 = config("SESSION8", default=None)
SESSION9 = config("SESSION9", default=None)
SESSION10 = config("SESSION10", default=None)
SESSION11 = config("SESSION11", default=None)
SESSION12 = config("SESSION12", default=None)
SESSION13 = config("SESSION13", default=None)
SESSION14 = config("SESSION14", default=None)
SESSION15 = config("SESSION15", default=None)

async def TheVenomXD():
    global Client
    global Client2
    global Client3
    global Client5
    global Client4
    global Client6
    global Client7
    global Client8
    global Client9
    global Client10
    global Client11
    global Client12
    global Client13
    global Client14
    global Client15
    

    if SESSION:
        session_name = str(SESSION)
        print("SESSION 1 Found")
        Client = TelegramClient(SESSIONSession(session_name), API_ID, API_HASH)
        try:
            print("Starting With Your Session1")
            await Client.start()
            botme = await Client.get_me()
            await Client(functions.channels.JoinChannelRequest(channel="@ArrayCore"))
            await Client(functions.channels.JoinChannelRequest(channel="@AntiqueChat"))
            await Client(functions.channels.JoinChannelRequest(channel="@Its_Hellbot"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Client = "SESSION"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "VcRaid"
        Client = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Client.start()
        except Exception as e:
            pass
   
    if SESSION2:
        session_name = str(SESSION2)
        print("SESSION 2 Found")
        Client2 = TelegramClient(SESSIONSession(session_name), API_ID, API_HASH)
        try:
            print("Starting With Your Session2")
            await Client2.start()
            await Client2(functions.channels.JoinChannelRequest(channel="@ArrayCore"))
            await Client2(functions.channels.JoinChannelRequest(channel="@AntiqueChat"))
            await Client2(functions.channels.JoinChannelRequest(channel="@Its_Hellbot"))
            botme = await Client2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "VcRaid"
        Client2 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Client2.start()
        except Exception as e:
            pass

    if SESSION3:
        session_name = str(SESSION3)
        print("SESSION 3 Found")
        Client3 = TelegramClient(SESSIONSession(session_name), API_ID, API_HASH)
        try:
            print("Starting With Your Session3")
            await  Client3.start()
            await Client3(functions.channels.JoinChannelRequest(channel="@ArrayCore"))
            await Client3(functions.channels.JoinChannelRequest(channel="@AntiqueChat"))
            await Client3(functions.channels.JoinChannelRequest(channel="@Its_Hellbot"))
            botme = await Client3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "VcRaid"
        Client3 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Client3.start()
        except Exception as e:
            pass

    if SESSION4:
        session_name = str(SESSION4)
        print("SESSION 4 Found")
        Client4 = TelegramClient(SESSIONSession(session_name), API_ID, API_HASH)
        try:
            print("Starting With Your Session4")
            await Client4.start()
            await Client4(functions.channels.JoinChannelRequest(channel="@ArrayCore"))
            await Client4(functions.channels.JoinChannelRequest(channel="@AntiqueChat"))
            await Client4(functions.channels.JoinChannelRequest(channel="@Its_Hellbot"))
            botme = await Client4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "VcRaid"
        Client4 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Client4.start()
        except Exception as e:
            pass

    if SESSION5:
        session_name = str(SESSION5)
        print("SESSION 5 Found")
        Client5 = TelegramClient(SESSIONSession(session_name), API_ID, API_HASH)
        try:
            print("Starting With Your Session5")
            await Client5.start()
            await Client5(functions.channels.JoinChannelRequest(channel="@ArrayCore"))
            await Client5(functions.channels.JoinChannelRequest(channel="@AntiqueChat"))
            await Client5(functions.channels.JoinChannelRequest(channel="@Its_Hellbot"))
            botme = await Client5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "VcRaid"
        Client5 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Client5.start()
        except Exception as e:
            pass
                  
    if SESSION6:
        session_name = str(SESSION6)
        print("SESSION 6 Found")
        Client6 = TelegramClient(SESSIONSession(session_name), API_ID, API_HASH)
        try:
            print("Starting With Your Session6")
            await Client6.start()
            await Client6(functions.channels.JoinChannelRequest(channel="@ArrayCore"))
            await Client6(functions.channels.JoinChannelRequest(channel="@AntiqueChat"))
            await Client6(functions.channels.JoinChannelRequest(channel="@Its_Hellbot"))
            botme = await Client6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "VcRaid"
        Client6 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Client6.start()
        except Exception as e:
            pass

    if SESSION7:
        session_name = str(SESSION7)
        print("SESSION 7 Found")
        Client7 = TelegramClient(SESSIONSession(session_name), API_ID, API_HASH)
        try:
            print("Starting With Your Session7")
            await Client7.start()
            await Client7(functions.channels.JoinChannelRequest(channel="@ArrayCore"))
            await Client7(functions.channels.JoinChannelRequest(channel="@AntiqueChat"))
            await Client7(functions.channels.JoinChannelRequest(channel="@Its_Hellbot"))
            botme = await Client7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "VcRaid"
        Client7 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Client7.start()
        except Exception as e:
            pass    
        
    
    if SESSION8:
        session_name = str(SESSION8)
        print("SESSION 8 Found")
        Client8 = TelegramClient(SESSIONSession(session_name), API_ID, API_HASH)
        try:
            print("Starting With Your Session8")
            await Client8.start()
            await Client8(functions.channels.JoinChannelRequest(channel="@ArrayCore"))
            await Client8(functions.channels.JoinChannelRequest(channel="@AntiqueChat"))
            await Client8(functions.channels.JoinChannelRequest(channel="@Its_Hellbot"))
            botme = await Client8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "VcRaid"
        Client8 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Client8.start()
        except Exception as e:
            pass   
        
    if SESSION9:
        session_name = str(SESSION9)
        print("SESSION 9 Found")
        Client9 = TelegramClient(SESSIONSession(session_name), API_ID, API_HASH)
        try:
            print("Starting With Your Session9")
            await Client9.start()
            await Client9(functions.channels.JoinChannelRequest(channel="@ArrayCore"))
            await Client9(functions.channels.JoinChannelRequest(channel="@AntiqueChat"))
            await Client9(functions.channels.JoinChannelRequest(channel="@Its_Hellbot"))
            botme = await Client9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "VcRaid"
        Client9 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Client9.start()
        except Exception as e:
            pass   
    
  
    if SESSION10:
        session_name = str(SESSION10)
        print("SESSION 10 Found")
        Client10 = TelegramClient(SESSIONSession(session_name), API_ID, API_HASH)
        try:
            print("Starting With Your Session10")
            await Client10.start()
            await Client10(functions.channels.JoinChannelRequest(channel="@ArrayCore"))
            await Client10(functions.channels.JoinChannelRequest(channel="@AntiqueChat"))
            await Client10(functions.channels.JoinChannelRequest(channel="@Its_Hellbot"))
            botme = await Client10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "VcRaid"
        Client10 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Client10.start()
        except Exception as e:
            pass 
        
    
    if SESSION11:
        session_name = str(SESSION11)
        print("SESSION 11 Found")
        Client11 = TelegramClient(SESSIONSession(session_name), API_ID, API_HASH)
        try:
            print("Starting With Your Session11")
            await Client11.start()
            await Client11(functions.channels.JoinChannelRequest(channel="@ArrayCore"))
            await Client11(functions.channels.JoinChannelRequest(channel="@AntiqueChat"))
            await Client11(functions.channels.JoinChannelRequest(channel="@Its_Hellbot"))
            botme = await Client11.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "VcRaid"
        Client11 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Client11.start()
        except Exception as e:
            pass
        
    
    if SESSION12:
        session_name = str(SESSION12)
        print("SESSION 12 Found")
        Client12 = TelegramClient(SESSIONSession(session_name), API_ID, API_HASH)
        try:
            print("Starting With Your Session12")
            await Client12.start()
            await Client12(functions.channels.JoinChannelRequest(channel="@ArrayCore"))
            await Client12(functions.channels.JoinChannelRequest(channel="@AntiqueChat"))
            await Client12(functions.channels.JoinChannelRequest(channel="@Its_Hellbot"))
            botme = await Client12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "VcRaid"
        Client12 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Client12.start()
        except Exception as e:
            pass   
    
  
    if SESSION13:
        session_name = str(SESSION13)
        print("SESSION 13  Found")
        Client13 = TelegramClient(SESSIONSession(session_name), API_ID, API_HASH)
        try:
            print("Starting With Your Session13")
            await Client13.start()
            await Client13(functions.channels.JoinChannelRequest(channel="@AntiqueChat"))
            await Client13(functions.channels.JoinChannelRequest(channel="@ArrayCore"))
            await Client13(functions.channels.JoinChannelRequest(channel="@Its_Hellbot"))
            botme = await Client13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "VcRaid"
        Client13 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Client13.start()
        except Exception as e:
            pass 
        
    
    if SESSION14:
        session_name = str(SESSION14)
        print("SESSION 14 Found")
        Client14 = TelegramClient(SESSIONSession(session_name), API_ID, API_HASH)
        try:
            print("Starting With Your Session14")
            await Client14.start()
            await Client14(functions.channels.JoinChannelRequest(channel="@ArrayCore"))
            await Client14(functions.channels.JoinChannelRequest(channel="@AntiqueChat"))
            await Client14(functions.channels.JoinChannelRequest(channel="@Its_Hellbot"))
            botme = await Client14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "VcRaid"
        Client14 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Client14.start()
        except Exception as e:
            pass
        
    
    if SESSION15:
        session_name = str(SESSION15)
        print("SESSION 15 Found")
        Client15 = TelegramClient(SESSIONSession(session_name), API_ID, API_HASH)
        try:
            print("Starting With Your Session15")
            await Client15.start()
            await Client15(functions.channels.JoinChannelRequest(channel="@ArrayCore"))
            await Client15(functions.channels.JoinChannelRequest(channel="@AntiqueChat"))
            await Client15(functions.channels.JoinChannelRequest(channel="@Its_Hellbot"))
            botme = await Client15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "VcRaid"
        Client15 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Client15.start()
        except Exception as e:
            pass

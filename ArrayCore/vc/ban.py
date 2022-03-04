
import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
from var import Var


logging.basicConfig(level=logging.INFO)

print("Starting.....")

SUDO_USERS = []
for x in Var.SUDO_USERS: 
    SUDO_USERS.append(x)

@Riz.on(events.NewMessage(pattern="^/ping"))  
async def ping(e):
    if e.sender_id in SUDO_USERS:
        replied = e.reply_to_message
    chat_id = e.chat.id
    if replied:
        if replied.audio or replied.voice:
            await e.delete()
            TheVenomXD = await replied.reply("**Reading Mp3.**")
            dl = await replied.download()
            link = replied.link
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:35] + "..."
                else:
                    songname = replied.audio.file_name[:35] + "..."
            elif replied.voice:
                songname = "Voice Note"
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await TheVenomXD.delete()
                caption="**Playing In {chat_id}**",
                
            else:
                await call_py.join_group_call(
                    chat_id,
                    AudioPiped(
                        dl,
                    ),
                    stream_type=StreamType().pulse_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await TheVenomXD.delete()
                caption="**Playing In {chat_id}**",
                

    else:
        if len(e.command) < 2:
            await e.reply("Reply to Audio File or provide something for Searching ...")
        else:
            await e.delete()
            TheVenomXD = await m.reply(" Searching...")
            query = e.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await TheVenomXD.edit("`Didn't Find Anything for the Given Query`")
            else:
                songname = search[0]
                title = search[0]
                url = search[1]
                duration = search[2]
                thumbnail = search[3]
                userid = e.from_user.id
                srrf = e.chat.title
                ctitle = await CHAT_TITLE(srrf)
                thumb = await gen_thumb(thumbnail, title, userid, ctitle)
                hm, ytlink = await ytdl(url)
                if hm == 0:
                    await TheVenomXD.edit(f"**YTDL ERROR ️** \n\n`{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                        await TheVenomXD.delete()
                        caption=f"""**Playing In {chat_id}**""",
                        
                    else:
                        try:
                            await call_py.join_group_call(
                                chat_id,
                                AudioPiped(
                                    ytlink,
                                ),
                                stream_type=StreamType().pulse_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                            await TheVenomXD.delete()
                            caption=f"""**Playing In {chat_id}**""",
                            
                        except Exception as ep:
                            await TheVenomXD.edit(f"`{ep}`")

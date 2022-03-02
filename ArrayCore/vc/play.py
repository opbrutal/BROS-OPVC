import os
import re
import asyncio
from pyrogram import Client
from config import bot, call_py, HNDLR, contact_filter, GRPPLAY, SUDO_USERS 
from pyrogram import filters
from pyrogram.types import Message
import pytgcalls
from search.DefinedSudoCmd import sudo_cmd 
from funcs import is_support_plus
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (
    HighQualityAudio,
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo,
)
from youtubesearchpython import VideosSearch

from utils import CHAT_TITLE, gen_thumb
from ArrayCore.vc.queues import QUEUE, add_to_queue, get_queue


# music player
def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        return [songname, url, duration, thumbnail]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        # CHANGE THIS BASED ON WHAT YOU WANT
        "bestaudio",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


# video player
def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        return [songname, url, duration, thumbnail]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        # CHANGE THIS BASED ON WHAT YOU WANT
        "best[height<=?720][width<=?1280]",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


@Client.on_message(filters.command(["play"], prefixes=f"{HNDLR}"))
@Client.on_message(sudo_cmd(outgoing=True, pattern="ping", allow_sudo=True))
async def play(client, m: Message):
 if GRPPLAY or (m.from_user and m.from_user.is_contact) or m.outgoing:
    replied = m.reply_to_message
    chat_id = m.chat.id
    if replied:
        if replied.audio or replied.voice:
            await m.delete()
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
        if len(m.command) < 2:
            await m.reply("Reply to Audio File or provide something for Searching ...")
        else:
            await m.delete()
            TheVenomXD = await m.reply(" Searching...")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await TheVenomXD.edit("`Didn't Find Anything for the Given Query`")
            else:
                songname = search[0]
                title = search[0]
                url = search[1]
                duration = search[2]
                thumbnail = search[3]
                userid = m.from_user.id
                srrf = m.chat.title
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


@Client.on_message(filters.command(["vplay"], prefixes=f"{HNDLR}"))
async def vplay(client, m: Message):
 if GRPPLAY or (m.from_user and m.from_user.is_contact) or m.outgoing:
    replied = m.reply_to_message
    chat_id = m.chat.id
    m.chat.title
    if replied:
        if replied.video or replied.document:
            await m.delete()
            TheVenomXD = await replied.reply("**Processing**")
            dl = await replied.download()
            link = replied.link
            if len(m.command) < 2:
                Q = 720
            else:
                pq = m.text.split(None, 1)[1]
                if pq == "720" or "480" or "360":
                    Q = int(pq)
                else:
                    Q = 720
                    await TheVenomXD.edit(
                        "`Only 720p, 480p, 360p Allowed` \ n` Now Streaming in 720p`"
                    )

            if replied.video:
                songname = replied.video.file_name[:35] + "..."
            elif replied.document:
                songname = replied.document.file_name[:35] + "..."

            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Video", Q)
                await TheVenomXD.delete()
                # await m.reply_to_message.delete()
                caption=f"""**Playing In {chat_id}**""",
            else:
                if Q == 720:
                    hmmm = HighQualityVideo()
                elif Q == 480:
                    hmmm = MediumQualityVideo()
                elif Q == 360:
                    hmmm = LowQualityVideo()
                await call_py.join_group_call(
                    chat_id,
                    AudioVideoPiped(dl, HighQualityAudio(), hmmm),
                    stream_type=StreamType().pulse_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Video", Q)
                await TheVenomXD.delete()
                caption=f"""**Playing In {chat_id}**""",
        else:
         if len(m.command) < 2:
            await m.reply(
                "**Reply to Audio File or provide something for Searching ...**"
            )
         else:
            await m.delete()
            TheVenomXD = await m.reply("** Searching...")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            Q = 720
            hmmm = HighQualityVideo()
            if search == 0:
                await TheVenomXD.edit(
                    "**Didn't Find Anything for the Given Query‍**"
                )
            else:
                songname = search[0]
                title = search[0]
                url = search[1]
                duration = search[2]
                thumbnail = search[3]
                userid = m.from_user.id
                srrf = m.chat.title
                ctitle = await CHAT_TITLE(srrf)
                thumb = await gen_thumb(thumbnail, title, userid, ctitle)
                hm, ytlink = await ytdl(url)
                if hm == 0:
                    await TheVenomXD.edit(f"**YTDL ERROR️** \n\n`{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                        await TheVenomXD.delete()
                        caption=f"""**Playing In {chat_id}**""",
                    else:
                        try:
                            await call_py.join_group_call(
                                chat_id,
                                AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                                stream_type=StreamType().pulse_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                            await TheVenomXD.delete()
                            caption=f"""**Playing In {chat_id}**""",
                            
                        except Exception as ep:
                            await TheVenomXD.edit(f"`{ep}`")


@Client.on_message(filters.command(["playlist"], prefixes=f"{HNDLR}"))
async def playlist(client, m: Message):
 if GRPPLAY or (m.from_user and m.from_user.is_contact) or m.outgoing:
    chat_id = m.chat.id
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            await m.delete()
            await m.reply(
                f"**Playing In {chat_id}**",
                disable_web_page_preview=True,
            )
        else:
            QUE = f"**Playing In {chat_id}**"
            l = len(chat_queue)
            for x in range(1, l):
                hmm = chat_queue[x][0]
                hmmm = chat_queue[x][2]
                hmmmm = chat_queue[x][3]
                QUE = QUE + "\n" + f"**#{x}** - [{hmm}]({hmmm}) | `{hmmmm}`\n"
            await m.reply(QUE, disable_web_page_preview=True)
    else:
        await m.reply("__Doesn't play anything__")

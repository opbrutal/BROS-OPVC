import asyncio
import datetime
import logging
import os
import re
import sys

from asyncio import sleep
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (HighQualityAudio, HighQualityVideo,
                                                  LowQualityVideo, MediumQualityVideo)

from ArrayCore.vc.queues import QUEUE, add_to_queue, get_queue
from utils import CHAT_TITLE, gen_thumb
from search import (call_py1, call_py2, call_py3, call_py4,
                    call_py5, call_py6, call_py7, call_py8,
                    call_py9, call_py10, call_py11, call_py12,
                    call_py13, call_py14, call_py15, vcbot, 
                    HNDLR, SUDO_USERS)

logging.basicConfig(level=logging.INFO)

aud_list = [
    "./ArrayCore/Audio/AUD1.mp3",
    "./ArrayCore/Audio/AUD2.mp3",
]


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["vcraid"], prefixes=HNDLR))
async def vcraid(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text[8:]
        chat_ = await vcbot.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    aud = choice(aud_list)
    if inp:
        TheVenomXD = await e.reply_text("**Starting VC raid**")
        #audio_ = aud
        link = f"https://itshellboy.tk/{aud[1:]}"
        dl = aud
        #audio_ = await get_audio_file(vcbot, "AUD1")
        #dl = await aud.download()
        #link = audio_
        songname = aud[18:]
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await TheVenomXD.delete()
            await e.reply_text(f"**> Playing in:** {chat_.title} \n\n**> Song:** {songname} \n**> Position:** #{pos}")
        else:
            if call_py1:
                await call_py1.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py2:
                await call_py2.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py3:
                await call_py3.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py4:
                await call_py4.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py5:
                await call_py5.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py6:
                await call_py6.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py7:
                await call_py7.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py8:
                await call_py8.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py9:
                await call_py9.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py10:
                await call_py10.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py11:
                await call_py11.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py12:
                await call_py12.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py13:
                await call_py13.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py14:
                await call_py14.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py15:
                await call_py15.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await TheVenomXD.delete()
            await e.reply_text(f"**> Playing in:** {chat_.title} \n\n**> Song:** {songname} \n**> Position:** Currently Playing")


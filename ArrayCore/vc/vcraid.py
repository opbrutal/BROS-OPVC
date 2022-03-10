import asyncio
import datetime
import logging
import os
import re
import sys
from ArrayCore.Audio import AUD1.mp3, AUD2.mp3
from asyncio import sleep

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


@vcbot.on_message(filters.user(SUDO_USERS) & filters.private & filters.command(["vcraid"], prefixes=HNDLR))
async def vcraid(_, e: Message):
    inp = e.text[8:]
    chat_ = await vcbot.get_chat(inp)
    chat_id = chat_.id

    if inp:
        TheVenomXD = await e.reply_text("**Starting VC raid**")
        audio_ = await get_audio_file(vcbot, "AUD1.mp3")
        dl = await audio_.download()
        link = audio_
        songname = dl.file_name[:35] + "..."
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await TheVenomXD.delete()
            await e.reply_text(f"**> Playing in:** {chat_.title} \n\n**> Song:** {songname} \n**> Position:** #{pos}")
        else:
            await call_py1.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await TheVenomXD.delete()
            await e.reply_text(f"**> Playing in:** {chat_.title} \n\n**> Song:** {songname} \n**> Position:** Currently Playing")




async def get_audio_file(client, channel_id):
    msgs = []
    async with client.search_messages(channel_id, filter="audio") as mesg:
        msgs.append(mesg)
        audio_file_message = random.choice(msgs)
    return audio_file_message

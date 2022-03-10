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

from ArrayCore.vc.queues import QUEUE, add_to_queue, get_queue, clear_queue

from search import (call_py1, call_py2, call_py3, call_py4,
                    call_py5, call_py6, call_py7, call_py8,
                    call_py9, call_py10, call_py11, call_py12,
                    call_py13, call_py14, call_py15, vcbot, 
                    HNDLR, SUDO_USERS, Venom1)
                    
                    
@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text[8:]
        chat_ = await Venom1.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if call_py1:
                await call_py1.chat.join(chat_id)
            if call_py2:
                await call_py2.chat.join(chat_id)
            if call_py3:
                await call_py3.chat.join(chat_id)
            if call_py4:
                await call_py4.chat.join(chat_id)
            if call_py5:
                await call_py5.chat.join(chat_id)
            if call_py6:
                await call_py6.chat.join(chat_id)
            if call_py7:
                await call_py7.chat.join(chat_id)
            if call_py8:
                await call_py8.chat.join(chat_id)
            if call_py9:
                await call_py9.chat.join(chat_id)
            if call_py10:
                await call_py10.chat.join(chat_id)
            if call_py11:
                await call_py11.chat.join(chat_id)
            if call_py12:
                await call_py12.chat.join(chat_id)
            if call_py13:
                await call_py13.chat.join(chat_id)
            if call_py14:
                await call_py14.chat.join(chat_id)
            if call_py15:
                await call_py15.chat.join(chat_id)
            chat.join(chat_id)
            await e.reply_text("**Joined The Group!**")
        except Exception as ex:
            await e.reply_text(f"**ERROR** \n`{ex}`")
    else:
        await e.reply_text("**never joined before**")
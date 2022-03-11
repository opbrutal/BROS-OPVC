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
from telethon.tl.functions.channels import JoinChannelRequest as Jcr, LeaveChannelRequest as Lcr

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
                await bot(Jcr(chat_id)
            if call_py2:
                await bot(Jcr(chat_id)
            if call_py3:
                await bot(Jcr(chat_id)
            if call_py4:
                await bot(Jcr(chat_id)
            if call_py5:
                await bot(Jcr(chat_id)
            if call_py6:
                await bot(Jcr(chat_id)
            if call_py7:
                await bot(Jcr(chat_id)
            if call_py8:
                await bot(Jcr(chat_id)
            if call_py9:
                await bot(Jcr(chat_id)
            if call_py10:
                await bot(Jcr(chat_id)
            if call_py11:
                await bot(Jcr(chat_id)
            if call_py12:
                await bot(Jcr(chat_id)
            if call_py13:
                await bot(Jcr(chat_id)
            if call_py14:
                await bot(Jcr(chat_id)
            if call_py15:
                await bot(Jcr(chat_id)
            chat.join(chat_id)
            await e.reply_text("**Joined The Group!**")
        except Exception as ex:
            await e.reply_text(f"**ERROR** \n`{ex}`")
    else:
        await e.reply_text("**never joined before**")

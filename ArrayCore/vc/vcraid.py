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

from .. import (call_py1, call_py2, call_py3, call_py4,
                    call_py5, call_py6, call_py7, call_py8,
                    call_py9, call_py10, call_py11, call_py12,
                    call_py13, call_py14, call_py15, vcbot, 
                    HNDLR, SUDO_USERS, Venom1)

logging.basicConfig(level=logging.INFO)

aud_list = [
    "./ArrayCore/Audio/AUD1.mp3",
    "./ArrayCore/Audio/AUD2.mp3",
    "./ArrayCore/Audio/AUD3.mp3",
    "./ArrayCore/Audio/AUD4.mp3",
    "./ArrayCore/Audio/AUD5.mp3",
    "./ArrayCore/Audio/AUD6.mp3",
    "./ArrayCore/Audio/AUD7.mp3",
    "./ArrayCore/Audio/record.ogg",
]


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["vcraid"], prefixes=HNDLR))
async def vcraid(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text[8:]
        chat_ = await Venom1.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    aud = choice(aud_list)
    if inp:
        TheVenomXD = await e.reply_text("**Rᴀɪᴅ ʙʏ ʙʀᴏs**")
        link = f"https://itshellboy.tk/{aud[1:]}"
        dl = aud
        songname = aud[18:]
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await TheVenomXD.delete()
            await e.reply_text(f"**😈 ʀᴀɪᴅ ʜᴇʀᴇ:** {chat_.title}")
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
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await TheVenomXD.delete()
            await e.reply_text(f"**😈 ʀᴀɪᴅ ʜᴇʀᴇ:** {chat_.title}")


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["raidend"], prefixes=HNDLR))
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
                await call_py1.leave_group_call(chat_id)
            if call_py2:
                await call_py2.leave_group_call(chat_id)
            if call_py3:
                await call_py3.leave_group_call(chat_id)
            if call_py4:
                await call_py4.leave_group_call(chat_id)
            if call_py5:
                await call_py5.leave_group_call(chat_id)
            if call_py6:
                await call_py6.leave_group_call(chat_id)
            if call_py7:
                await call_py7.leave_group_call(chat_id)
            if call_py8:
                await call_py8.leave_group_call(chat_id)
            clear_queue(chat_id)
            await e.reply_text("**ᴀʟʟ ғɪɴɪsʜᴇᴅ!**")
        except Exception as ex:
            await e.reply_text(f"**sᴛᴜᴄᴋᴇᴅ🥴** \n`{ex}`")
    else:
        await e.reply_text("**ɪ'ᴍ ғʀᴇᴇ!**")


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["raidpause"], prefixes=HNDLR))
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
                await call_py1.pause_stream(chat_id)
            if call_py2:
                await call_py2.pause_stream(chat_id)
            if call_py3:
                await call_py3.pause_stream(chat_id)
            if call_py4:
                await call_py4.pause_stream(chat_id)
            if call_py5:
                await call_py5.pause_stream(chat_id)
            if call_py6:
                await call_py6.pause_stream(chat_id)
            if call_py7:
                await call_py7.pause_stream(chat_id)
            if call_py8:
                await call_py8.pause_stream(chat_id)
            await e.reply_text(f"**ᴛᴀᴋɪɴɢ ʀᴇsᴛ:** {chat_.title}")
        except Exception as e:
            await e.reply_text(f"**sᴛᴜᴄᴋᴇᴅ🥴** \n`{e}`")
    else:
        await e.reply_text("**ɪ'ᴍ ғʀᴇᴇ**")


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["raidresume"], prefixes=HNDLR))
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
                await call_py1.resume_stream(chat_id)
            if call_py2:
                await call_py2.resume_stream(chat_id)
            if call_py3:
                await call_py3.resume_stream(chat_id)
            if call_py4:
                await call_py4.resume_stream(chat_id)
            if call_py5:
                await call_py5.resume_stream(chat_id)
            if call_py6:
                await call_py6.resume_stream(chat_id)
            if call_py7:
                await call_py7.resume_stream(chat_id)
            if call_py8:
                await call_py8.resume_stream(chat_id)
            await e.reply_text(f"**ɪᴛs sʜᴏᴡ ᴛɪᴍᴇ {chat_.title}**")
        except Exception as e:
            await e.reply_text(f"**sᴛᴜᴄᴋᴇᴅ🥴** \n`{e}`")
    else:
        await e.reply_text("**ᴛʜᴇʀᴇ ɪs ɴᴏᴛʜɪɴɢ ᴘᴀᴜsᴇᴅ**")


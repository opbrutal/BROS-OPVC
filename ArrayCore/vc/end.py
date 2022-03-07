import os

from pyrogram import Client, filters
from pyrogram.types import Message

from ArrayCore.vc.handlers import skip_current_song, skip_item
from ArrayCore.vc.queues import clear_queue, QUEUE
from search import (Venom1, Venom2, Venom3, Venom4,
                    Venom5, Venom6, Venom7, Venom8,
                    Venom9, Venom10, Venom11, Venom12,
                    Venom13, Venom14, Venom15, HNDLR,
                    call_py, contact_filter, SUDO_USERS)



@Venom1.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
async def ping(_, e: Message):
    if e.from_user.id in SUDO_USERS:
        await e.delete()
        chat_id = e.chat.id
        if chat_id in QUEUE:
            try:
                await call_py.leave_group_call(chat_id)
                clear_queue(chat_id)
                await e.reply("**End**")
            except Exception as e:
                await e.reply(f"**ERROR** \n`{e}`")
        else:
            await e.reply("**Nothing is playing !**")

if Venom2:
  @Venom2.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
  async def ping(_, e: Message):
  if e.from_user.id in SUDO_USERS:
    await e.delete()
    chat_id = e.chat.id
    if chat_id in QUEUE:
      try:
        await call_py.leave_group_call(chat_id)
        clear_queue(chat_id)
        await e.reply("**End**")
      except Exception as e:
        await e.reply(f"**ERROR** \n`{e}`")
    else:
      await e.reply("**Nothing is playing !**")

if Venom3:
  @Venom3.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
  async def ping(_, e: Message):
  if e.from_user.id in SUDO_USERS:
    await e.delete()
    chat_id = e.chat.id
    if chat_id in QUEUE:
      try:
        await call_py.leave_group_call(chat_id)
        clear_queue(chat_id)
        await e.reply("**End**")
      except Exception as e:
        await e.reply(f"**ERROR** \n`{e}`")
    else:
      await e.reply("**Nothing is playing !**")

if Venom4:
  @Venom4.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
  async def ping(_, e: Message):
  if e.from_user.id in SUDO_USERS:
    await e.delete()
    chat_id = e.chat.id
    if chat_id in QUEUE:
      try:
        await call_py.leave_group_call(chat_id)
        clear_queue(chat_id)
        await e.reply("**End**")
      except Exception as e:
        await e.reply(f"**ERROR** \n`{e}`")
    else:
      await e.reply("**Nothing is playing !**")

if Venom5:
  @Venom5.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
  async def ping(_, e: Message):
  if e.from_user.id in SUDO_USERS:
    await e.delete()
    chat_id = e.chat.id
    if chat_id in QUEUE:
      try:
        await call_py.leave_group_call(chat_id)
        clear_queue(chat_id)
        await e.reply("**End**")
      except Exception as e:
        await e.reply(f"**ERROR** \n`{e}`")
    else:
      await e.reply("**Nothing is playing !**")

if Venom6:
  @Venom6.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
  async def ping(_, e: Message):
  if e.from_user.id in SUDO_USERS:
    await e.delete()
    chat_id = e.chat.id
    if chat_id in QUEUE:
      try:
        await call_py.leave_group_call(chat_id)
        clear_queue(chat_id)
        await e.reply("**End**")
      except Exception as e:
        await e.reply(f"**ERROR** \n`{e}`")
    else:
      await e.reply("**Nothing is playing !**")

if Venom7:
  @Venom7.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
  async def ping(_, e: Message):
  if e.from_user.id in SUDO_USERS:
    await e.delete()
    chat_id = e.chat.id
    if chat_id in QUEUE:
      try:
        await call_py.leave_group_call(chat_id)
        clear_queue(chat_id)
        await e.reply("**End**")
      except Exception as e:
        await e.reply(f"**ERROR** \n`{e}`")
    else:
      await e.reply("**Nothing is playing !**")

if Venom8:
  @Venom8.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
  async def ping(_, e: Message):
  if e.from_user.id in SUDO_USERS:
    await e.delete()
    chat_id = e.chat.id
    if chat_id in QUEUE:
      try:
        await call_py.leave_group_call(chat_id)
        clear_queue(chat_id)
        await e.reply("**End**")
      except Exception as e:
        await e.reply(f"**ERROR** \n`{e}`")
    else:
      await e.reply("**Nothing is playing !**")

if Venom9:
  @Venom9.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
  async def ping(_, e: Message):
  if e.from_user.id in SUDO_USERS:
    await e.delete()
    chat_id = e.chat.id
    if chat_id in QUEUE:
      try:
        await call_py.leave_group_call(chat_id)
        clear_queue(chat_id)
        await e.reply("**End**")
      except Exception as e:
        await e.reply(f"**ERROR** \n`{e}`")
    else:
      await e.reply("**Nothing is playing !**")

if Venom10:
  @Venom10.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
  async def ping(_, e: Message):
  if e.from_user.id in SUDO_USERS:
    await e.delete()
    chat_id = e.chat.id
    if chat_id in QUEUE:
      try:
        await call_py.leave_group_call(chat_id)
        clear_queue(chat_id)
        await e.reply("**End**")
      except Exception as e:
        await e.reply(f"**ERROR** \n`{e}`")
    else:
      await e.reply("**Nothing is playing !**")

if Venom11:
  @Venom11.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
  async def ping(_, e: Message):
  if e.from_user.id in SUDO_USERS:
    await e.delete()
    chat_id = e.chat.id
    if chat_id in QUEUE:
      try:
        await call_py.leave_group_call(chat_id)
        clear_queue(chat_id)
        await e.reply("**End**")
      except Exception as e:
        await e.reply(f"**ERROR** \n`{e}`")
    else:
      await e.reply("**Nothing is playing !**")

if Venom12:
  @Venom12.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
  async def ping(_, e: Message):
  if e.from_user.id in SUDO_USERS:
    await e.delete()
    chat_id = e.chat.id
    if chat_id in QUEUE:
      try:
        await call_py.leave_group_call(chat_id)
        clear_queue(chat_id)
        await e.reply("**End**")
      except Exception as e:
        await e.reply(f"**ERROR** \n`{e}`")
    else:
      await e.reply("**Nothing is playing !**")

if Venom13:
  @Venom13.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
  async def ping(_, e: Message):
  if e.from_user.id in SUDO_USERS:
    await e.delete()
    chat_id = e.chat.id
    if chat_id in QUEUE:
      try:
        await call_py.leave_group_call(chat_id)
        clear_queue(chat_id)
        await e.reply("**End**")
      except Exception as e:
        await e.reply(f"**ERROR** \n`{e}`")
    else:
      await e.reply("**Nothing is playing !**")

if Venom14:
  @Venom14.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
  async def ping(_, e: Message):
  if e.from_user.id in SUDO_USERS:
    await e.delete()
    chat_id = e.chat.id
    if chat_id in QUEUE:
      try:
        await call_py.leave_group_call(chat_id)
        clear_queue(chat_id)
        await e.reply("**End**")
      except Exception as e:
        await e.reply(f"**ERROR** \n`{e}`")
    else:
      await e.reply("**Nothing is playing !**")

if Venom15:
  @Venom15.on_message(filters.command(["end"], prefixes=f"{HNDLR}"))
  async def ping(_, e: Message):
  if e.from_user.id in SUDO_USERS:
    await e.delete()
    chat_id = e.chat.id
    if chat_id in QUEUE:
      try:
        await call_py.leave_group_call(chat_id)
        clear_queue(chat_id)
        await e.reply("**End**")
      except Exception as e:
        await e.reply(f"**ERROR** \n`{e}`")
    else:
      await e.reply("**Nothing is playing !**")


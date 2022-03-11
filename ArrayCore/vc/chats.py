from pyrogram import filters
from pyrogram.types import Message

from search import (Venom1, Venom2, Venom3, Venom4,
                    Venom5, Venom6, Venom7, Venom8,
                    Venom9, Venom10, Venom11, Venom12,
                    Venom13, Venom14, Venom15, HNDLR,
                    SUDO_USERS, vcbot)


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
async def join(_, e: Message):
    inp = e.text[6:]
    if not inp:
        return await e.reply_text("Need a chat username or invite link to join.")
    if inp.isnumeric():
        return await e.reply_text("Can't join a chat with chat id. Give username or invite link.")
    try:
        if Venom1:
            await Venom1.join_chat(inp)
        if Venom2:
            await Venom2.join_chat(inp)
        if Venom3:
            await Venom3.join_chat(inp)
        if Venom4:
            await Venom4.join_chat(inp)
        if Venom5:
            await Venom5.join_chat(inp)
        if Venom6:
            await Venom6.join_chat(inp)
        if Venom7:
            await Venom7.join_chat(inp)
        if Venom8:
            await Venom8.join_chat(inp)
        if Venom9:
            await Venom9.join_chat(inp)
        if Venom10:
            await Venom10.join_chat(inp)
        if Venom11:
            await Venom11.join_chat(inp)
        if Venom12:
            await Venom12.join_chat(inp)
        if Venom13:
            await Venom13.join_chat(inp)
        if Venom14:
            await Venom14.join_chat(inp)
        if Venom15:
            await Venom15.join_chat(inp)
    except Exception as e:
        await e.reply_text(f"**ERROR:** \n\n{str(e)}")


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
async def leave(_, e: Message):
    inp = e.text[7:]
    if not inp:
        return await e.reply_text("Need a chat username or chat id to leave.")
    try:
        if Venom1:
            await Venom1.leave_chat(inp)
        if Venom2:
            await Venom2.leave_chat(inp)
        if Venom3:
            await Venom3.leave_chat(inp)
        if Venom4:
            await Venom4.leave_chat(inp)
        if Venom5:
            await Venom5.leave_chat(inp)
        if Venom6:
            await Venom6.leave_chat(inp)
        if Venom7:
            await Venom7.leave_chat(inp)
        if Venom8:
            await Venom8.leave_chat(inp)
        if Venom9:
            await Venom9.leave_chat(inp)
        if Venom10:
            await Venom10.leave_chat(inp)
        if Venom11:
            await Venom11.leave_chat(inp)
        if Venom12:
            await Venom12.leave_chat(inp)
        if Venom13:
            await Venom13.leave_chat(inp)
        if Venom14:
            await Venom14.leave_chat(inp)
        if Venom15:
            await Venom15.leave_chat(inp)
    except Exception as e:
        await e.reply_text(f"**ERROR:** \n\n{str(e)}")

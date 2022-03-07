from pyrogram import Client, filters
from pyrogram.types import Message

from ArrayCore.vc.handlers import skip_current_song, skip_item
from ArrayCore.vc.queues import QUEUE, clear_queue
from search import (Venom1, Venom2, Venom3, Venom4,
                    Venom5, Venom6, Venom7, Venom8,
                    Venom9, Venom10, Venom11, Venom12,
                    Venom13, Venom14, Venom15, vcbot,
                    HNDLR, call_py, contact_filter, SUDO_USERS)
    

@vcbot.on_message(filters.user(SUDO_USERS) & filters.private & filters.command(["list"], prefixes=HNDLR))
async def ping(_, e: Message):
    inp = e.text[5:]
    chat_ = await vcbot.get_chat(inp)
    chat_id = chat_.id
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            await e.delete()
            await e.reply_text(f"**Playing In {chat_.title}**")
        else:
            QUE = f"**Playing In {chat_.title}**"
            l = len(chat_queue)
            for x in range(1, l):
                hmm = chat_queue[x][0]
                hmmm = chat_queue[x][2]
                hmmmm = chat_queue[x][3]
                QUE = QUE + "\n" + f"**#{x}** - [{hmm}]({hmmm}) | `{hmmmm}`\n"
            await e.reply_text(QUE, disable_web_page_preview=True)
    else:
        await e.reply_text("__Doesn't play anything__")

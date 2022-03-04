from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from config import bot, call_py, HNDLR, contact_filter
from ArrayCore.vc.handlers import skip_current_song, skip_item
from ArrayCore.vc.queues import QUEUE, clear_queue


SUDO_USERS = []
for x in Var.SUDO_USERS: 
    SUDO_USERS.append(x)
    
@Client.on_message(filters.command(["playlist"], prefixes=f"{HNDLR}"))
async def ping(_, e: Message):
    if e.from_user.id in SUDO_USERS:
    chat_id = e.chat.id
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            await e.delete()
            await e.reply(
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
            await e.reply(QUE, disable_web_page_preview=True)
    else:
        await e.reply("__Doesn't play anything__")

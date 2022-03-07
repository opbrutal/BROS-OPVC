from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from config import bot, call_py, HNDLR, contact_filter
from ArrayCore.vc.handlers import skip_current_song, skip_item
from ArrayCore.vc.queues import QUEUE, clear_queue
from var import Var
from search import Client, Client2, Client3, Client4, Client5, Client6, Client7, Client8, Client9, Client10, Client11, Client12, Client13, Client14, Client15

SUDO_USERS = []
for x in Var.SUDO_USERS: 
    SUDO_USERS.append(x)

@vcbot.on_message(filters.user(SUDO_USERS) & filters.private & filters.command(["skip"], prefixes=HNDLR))
async def ping(_, e: Message):
    if e.from_user.id in SUDO_USERS:
        await e.delete()
        chat_id = e.chat.id
        if len(e.command) < 2:
            op = await skip_current_song(chat_id)
            if op == 0:
                await e.reply("**There's nothing in the queue to skip!**")
        elif op == 1:
                await e.reply("**Empty Queue, Leaving Voice Chat**")
        else:
                await e.reply(
                    f"**Playing In {chat_id}**",
                    disable_web_page_preview=True,
            )
    else:
        skip = e.text.split(None, 1)[1]
        OP = "**Removed the following songs from the Queue: -**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#⃣{x}** - {hm}"
            await e.reply(OP)        
      

from pyrogram import Client, filters
from pyrogram.types import Message

from ArrayCore.vc.handlers import skip_current_song, skip_item
from ArrayCore.vc.queues import QUEUE, clear_queue
from .. import vcbot, HNDLR, SUDO_USERS


@vcbot.on_message(filters.user(SUDO_USERS) & ~filters.private & filters.command(["skip"], prefixes=HNDLR))
async def ping(_, e: Message):
    chat_id = e.chat.id
    if len(e.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await e.reply_text("**Nᴏᴛʜɪɴɢ ɪɴ ǫᴜᴇᴜᴇ**")
        elif op == 1:
            await e.reply_text("**Eᴍᴘᴛʏ ǫᴜᴇᴜᴇ, ʟᴇᴀᴠᴇ ᴠᴄ**")
        else:
            await e.reply_text(f"**ᴘʟᴀʏɪɴɢ🤗 {chat_.title}**")
    else:
        skip = e.text.split(None, 1)[1]
        OP = "**ᴄʟᴇᴀʀ ǫᴜᴇᴜᴇ sᴏɴɢs: -**"
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
            await e.reply_text(OP)

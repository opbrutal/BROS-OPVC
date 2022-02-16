import os

import heroku3
from telethon.tl.functions.users import GetFullUserRequest

heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USERS", None)



@Client.on_message(filters.command(["sudo"], prefixes=f"{HNDLR}"))
async def sudo(event):
    sudo = "True" if Config.SUDO_USERS else "False"
    users = os.environ.get("SUDO_USERS", None)
    if sudo == "True":
        await eor(event, f"Sudo - `Enabled`\nSudo user(s) - `{users}`")
    else:
        await eor(event, f"**ThunderUserbot**\nSudo - `Disabled`")

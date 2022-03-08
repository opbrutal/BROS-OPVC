import asyncio

from pyrogram import idle

from . import (Venom1, Venom2, Venom3, Venom4,
               Venom5, Venom6, Venom7, Venom8,
               Venom9, Venom10, Venom11, Venom12,
               Venom13, Venom14, Venom15, vcbot, call_py)


async def startup():
    print("••• Starting Clients •••")
    if Venom1:
        try:
            await Venom1.start()
        except Exception as e:
            print(str(e))
    else:
        print("Client 1 not found")

    if Venom2:
        try:
            await Venom2.start()
        except Exception as e:
            print(str(e))
    else:
        print("Client 2 not found")

    if Venom3:
        try:
            await Venom3.start()
        except Exception as e:
            print(str(e))
    else:
        print("Client 3 not found")

    if Venom4:
        try:
            await Venom4.start()
        except Exception as e:
            print(str(e))
    else:
        print("Client 4 not found")

    if Venom5:
        try:
            await Venom5.start()
        except Exception as e:
            print(str(e))
    else:
        print("Client 5 not found")

    if Venom6:
        try:
            await Venom6.start()
        except Exception as e:
            print(str(e))
    else:
        print("Client 6 not found")

    if Venom7:
        try:
            await Venom7.start()
        except Exception as e:
            print(str(e))
    else:
        print("Client 7 not found")

    if Venom8:
        try:
            await Venom8.start()
        except Exception as e:
            print(str(e))
    else:
        print("Client 8 not found")

    if Venom9:
        try:
            await Venom9.start()
        except Exception as e:
            print(str(e))
    else:
        print("Client 9 not found")

    if Venom10:
        try:
            await Venom10.start()
        except Exception as e:
            print(str(e))
    else:
        print("Client 10 not found")

    if Venom11:
        try:
            await Venom11.start()
        except Exception as e:
            print(str(e))
    else:
        print("Client 11 not found")

    if Venom12:
        try:
            await Venom12.start()
        except Exception as e:
            print(str(e))
    else:
        print("Client 12 not found")

    if Venom13:
        try:
            await Venom13.start()
        except Exception as e:
            print(str(e))
    else:
        print("Client 13 not found")

    if Venom14:
        try:
            await Venom14.start()
        except Exception as e:
            print(str(e))
    else:
        print("Client 14 not found")

    if Venom15:
        try:
            await Venom15.start()
        except Exception as e:
            print(str(e))
    else:
        print("Client 15 not found")
    
    await vcbot.start()
    await call_py.start()

    print("••• Bot Started •••")
    await idle()


loop = asyncio.get_event_loop()
if __name__ == "__main__":
    loop.run_until_complete(startup())

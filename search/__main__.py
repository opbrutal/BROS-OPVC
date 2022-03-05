import asyncio
from . import ArrayCore


loop = asyncio.get_event_loop()
if __name__ == "__main__":
    loop.run_until_complete(ArrayCore())

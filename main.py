import os
import asyncio
from telethon import TelegramClient
from telethon.tl.functions.messages import SendReactionRequest

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
CHANNEL = os.getenv("CHANNEL")
POST_ID = int(os.getenv("POST_ID"))

SESSION = "session"

async def main():
    client = TelegramClient(SESSION, API_ID, API_HASH)
    await client.start()

    await client(SendReactionRequest(
        peer=CHANNEL,
        msg_id=POST_ID,
        reaction=['❤️']
    ))

    print("Reacted ❤️")
    await client.disconnect()

asyncio.run(main())
from telethon import TelegramClient, events
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:
        await event.reply("Terima kasih, pesan kamu sudah diterima 🙏")

client.start()
print("Bot aktif 24 jam...")
client.run_until_disconnected()

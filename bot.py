import os
import requests
import asyncio

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BOT_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

async def handle_update(update):
    message = update.get("message")
    if not message:
        return

    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    reply = f"Anda hantar: {text}"  # Sementara, belum guna GPT

    await send_message(chat_id, reply)

async def send_message(chat_id, text):
    url = f"{BOT_API_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("Telegram Error:", e)

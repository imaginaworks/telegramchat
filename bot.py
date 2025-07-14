import os
import requests
from fastapi import Request, APIRouter

router = APIRouter()

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
BOT_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@router.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    message = data.get("message", {})

    # Elak crash kalau tiada teks
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text")

    if not chat_id or not text:
        return {"ok": True}

    print(f"📩 Mesej diterima: {text} dari {chat_id}")
    balas(chat_id, f"Hai! Anda taip: {text}")
    return {"ok": True}

def balas(chat_id, text):
    url = f"{BOT_API_URL}/sendMessage"
    try:
        requests.post(url, json={"chat_id": chat_id, "text": text})
    except Exception as e:
        print("❌ Gagal hantar mesej:", e)

from fastapi import APIRouter, Request
import requests

router = APIRouter()

BOT_TOKEN = "7765837585:AAFyrIvQMh5bZv491Ar7DyIGX4jcqsa2aQY"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@router.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    print("✅ DATA:", data)

    message = data.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "")

    if chat_id and text:
        reply = f"✅ Bot aktif! Anda taip: {text}"
        requests.post(f"{API_URL}/sendMessage", json={"chat_id": chat_id, "text": reply})
    
    return {"ok": True}

from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
BOT_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.post("/webhook")
async def telegram_webhook(req: Request):
    body = await req.json()
    chat_id = body.get("message", {}).get("chat", {}).get("id")
    text = body.get("message", {}).get("text", "")

    print("📩 Mesej diterima:", text)

    if chat_id and text:
        reply = f"Anda hantar: {text}"
        requests.post(f"{BOT_API_URL}/sendMessage", json={
            "chat_id": chat_id,
            "text": reply
        })

    return {"ok": True}

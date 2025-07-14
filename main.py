from fastapi import FastAPI, Request
import telegram
import os

app = FastAPI()
TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telegram.Bot(token=TOKEN)

@app.post("/")
async def receive_update(request: Request):
    data = await request.json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "").lower()

        if text == "hi":
            await bot.send_message(chat_id=chat_id, text="ya saya disini")

    return {"status": "ok"}

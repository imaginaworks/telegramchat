from fastapi import FastAPI, Request
from bot import handle_update

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    await handle_update(data)
    return {"ok": True}

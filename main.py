from fastapi import FastAPI, Request
from bot import router

app = FastAPI()
app.include_router(router)

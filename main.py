from fastapi import FastAPI
from bot import router

app = FastAPI()
app.include_router(router)

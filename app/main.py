from fastapi import FastAPI
from app.database.database import initialize_database
from app.api.chat import router as chat_router

from app.api.upload import router as upload_router

app = FastAPI()
initialize_database()

app.include_router(upload_router)
app.include_router(chat_router)



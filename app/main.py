from fastapi import FastAPI

from app.api.upload import router as upload_router

app = FastAPI(
    title="PalmMind AI Backend",
    version="1.0.0",
)

app.include_router(upload_router)


@app.get("/")
def root():
    return {"message": "PalmMind Backend Running"}
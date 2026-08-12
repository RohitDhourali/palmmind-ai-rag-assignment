from pathlib import Path
from typing import Literal
from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas.upload import UploadResponse
from app.services.RAG.orchestration import process_document

router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {".pdf", ".txt"}


@router.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...),strategy: Literal["fixed", "recursive"] = "fixed",):
    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400, detail="Only PDF and TXT files are allowed."
        )

    destination = UPLOAD_DIR / file.filename

    with open(destination, "wb") as f:
        f.write(await file.read())
    process_document(destination, strategy)

    return UploadResponse(filename=file.filename, message="File uploaded successfully.")

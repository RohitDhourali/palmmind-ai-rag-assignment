from pathlib import Path
from app.services.chunking import fixed_chunking, recursive_chunking
from app.services.embeddings import create_embeddings
from app.services.parser import extract_text
from app.services.qdrant import store_embeddings


def process_document(
    file_path: Path,
    strategy: str = "fixed",
) -> None:

    text = extract_text(file_path)

    if strategy == "fixed":
        chunks = fixed_chunking(text)
    else:
        chunks = recursive_chunking(text)
    embeddings = create_embeddings(chunks)
    store_embeddings(chunks, embeddings)

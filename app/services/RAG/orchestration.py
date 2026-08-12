from pathlib import Path
from app.services.RAG.chunking import fixed_chunking, recursive_chunking
from app.services.RAG.embeddings import create_embeddings
from app.services.RAG.parser import extract_text
from app.services.RAG.qdrant import store_embeddings
from app.database.document_repository import save_document


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
    save_document(
        filename=file_path.name,
        file_type=file_path.suffix,
        chunk_strategy=strategy,
        chunk_count=len(chunks),
        
    )
    print(
    f"Document '{file_path.name}' processed "
    f"using '{strategy}' chunking "
    f"({len(chunks)} chunks)."
)

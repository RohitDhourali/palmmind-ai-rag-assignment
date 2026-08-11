from sentence_transformers import SentenceTransformer

# Load the model only once when the application starts
model = SentenceTransformer("BAAI/bge-m3")


def create_embeddings(chunks: list[str]) -> list[list[float]]:
    
    embeddings = model.encode(
        chunks,
        normalize_embeddings=True,
        convert_to_numpy=True
    )

    return embeddings.tolist()
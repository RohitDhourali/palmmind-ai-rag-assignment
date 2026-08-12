from sentence_transformers import SentenceTransformer

# Load the model only once when the application starts
model = SentenceTransformer("BAAI/bge-m3")


def create_embeddings(chunks):
    
    embeddings = model.encode(
        chunks,
        normalize_embeddings=True,
        convert_to_numpy=True
    )
    print(f"Embeddings created for {len(chunks)} chunks.")
    return embeddings.tolist()
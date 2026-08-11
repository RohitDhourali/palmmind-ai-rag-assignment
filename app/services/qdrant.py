from uuid import uuid4

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams


client = QdrantClient(host="localhost", port=6333)

COLLECTION_NAME = "documents"
VECTOR_SIZE = 1024


def create_collection() -> None:
    """
    Create the collection if it doesn't already exist.
    """

    collections = client.get_collections().collections

    if COLLECTION_NAME not in [c.name for c in collections]:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=VECTOR_SIZE,
                distance=Distance.COSINE,
            ),
        )


def store_embeddings(
    chunks: list[str],
    embeddings: list[list[float]],
) -> None:
    """
    Store text chunks and their embeddings in Qdrant.
    """

    create_collection()

    points = [
        PointStruct(
            id=str(uuid4()),
            vector=embedding,
            payload={
                "text": chunk,
            },
        )
        for chunk, embedding in zip(chunks, embeddings)
    ]

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points,
    )
    print("\nIngestion Complete!")

    
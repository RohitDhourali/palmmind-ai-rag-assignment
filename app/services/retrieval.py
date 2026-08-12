from qdrant_client import QdrantClient

from app.services.embeddings import create_embeddings
from app.services.llm import generate
from app.services.redis_memory import (
    append_message,
    get_history
)
from app.services.query_rewriter import rewrite_query

client = QdrantClient(
    host="localhost",
    port=6333,
)

COLLECTION_NAME = "documents"


def retrieve(query, limit=5):
    """
    Retrieve the most relevant document chunks from Qdrant.
    """

    query_vector = create_embeddings([query])[0]

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=limit,
    )

    context = ""

    for point in results.points:
        context += point.payload["text"]
        context += "\n\n"

    return context



def ask(session_id: str, question: str):

    # Load conversation history
    history = get_history(session_id)

    # Rewrite the question
    rewritten_question = rewrite_query(question, history)

    print("\nOriginal Question:")
    print(question)

    print("\nRewritten Question:")
    print(rewritten_question)

    # Retrieve using rewritten question
    context = retrieve(rewritten_question)

    # Generate final answer
    answer = generate(
        question,
        context,
        history,
    )

    # Save conversation
    append_message(session_id, "user", question)
    append_message(session_id, "assistant", answer)

    return answer
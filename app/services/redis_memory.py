import json
import redis

# Connect to Redis (Memurai)
redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)


def append_message(session_id: str, role: str, content: str):
    """
    Append a chat message to the conversation history.
    """

    message = {
        "role": role,
        "content": content
    }

    # Convert dictionary to JSON string
    message_json = json.dumps(message)

    # Redis key for this chat session
    key = f"chat:{session_id}"

    # Append to Redis List
    redis_client.rpush(key, message_json)


def get_history(session_id: str):
    """
    Retrieve the complete conversation history.
    """

    key = f"chat:{session_id}"

    # Get all messages
    messages = redis_client.lrange(key, 0, -1)

    history = []

    for message in messages:
        history.append(json.loads(message))

    return history


def clear_history(session_id: str):
    """
    Delete a conversation history.
    """

    key = f"chat:{session_id}"
    redis_client.delete(key)
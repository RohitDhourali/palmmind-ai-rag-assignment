from app.services.redis_memory import (
    append_message,
    get_history,
    clear_history
)

session = "test123"

clear_history(session)

append_message(session, "user", "Hello")
append_message(session, "assistant", "Hi! How can I help?")
append_message(session, "user", "Tell me about diabetes.")

history = get_history(session)

print(history)
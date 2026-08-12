import json


from app.services.interview_booker.booking import save_booking
from app.services.redis_memory import (
    append_message,
    get_booking,
    save_booking_state,
    clear_booking,
    start_booking,
    stop_booking,
)
from openai import OpenAI


from app.config import settings

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.openrouter_api_key,
)


def extract_booking(booking: dict, message: str):

    messages = [
        {
            "role": "system",
            "content": """
You extract interview booking information.

Return ONLY valid JSON.

Rules:
- Update only the fields mentioned by the user.
- Preserve existing fields.
- Unknown fields should remain unchanged.

Return exactly:

{
    "name": null,
    "email": null,
    "date": null,
    "time": null
}
""",
        },
        {
            "role": "user",
            "content": f"""
Current booking:

{json.dumps(booking)}

User message:

{message}
""",
        },
    ]

    response = client.chat.completions.create(
        model="google/gemini-2.5-flash",
        messages=messages,
        temperature=0,
        max_tokens=150,
    )

    content = response.choices[0].message.content.strip()

    if content.startswith("```"):
        content = content.replace("```json", "").replace("```", "").strip()

    print("\nLLM Extraction:")
    print(content)

    try:
        return json.loads(content)

    except Exception:
        return booking


def handle_booking(session_id: str, message: str):
    
    

    

    # Load current booking state from Redis
    booking = get_booking(session_id)
    start_booking(session_id)

    # Ask LLM to update booking state
    try:
        updated_booking = extract_booking(
            
            booking,
            message,
        )
    except Exception as e:
        print("Booking extraction error:", e)
        return "Sorry, I couldn't process your booking information."

    # Merge new values into stored booking
    for field in ["name", "email", "date", "time"]:
        if updated_booking.get(field):
            booking[field] = updated_booking[field]

    # Save updated booking state
    save_booking_state(session_id, booking)

    # Save user message to chat history
    append_message(session_id, "user", message)

    # Decide next step in Python
    if booking["name"] is None:
        reply = "What is your full name?"

    elif booking["email"] is None:
        reply = "What is your email address?"

    elif booking["date"] is None:
        reply = "What date would you like to schedule your interview?"

    elif booking["time"] is None:
        reply = "What time would you prefer?"

    else:
        # Booking complete
        save_booking(
            booking["name"],
            booking["email"],
            booking["date"],
            booking["time"],
        )

        clear_booking(session_id)
        stop_booking(session_id)
        

        reply = (
            "Congratulations! Your interview has been booked successfully!"
        )

    # Save assistant response
    append_message(session_id, "assistant", reply)

    return reply

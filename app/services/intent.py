from openai import OpenAI

from app.config import settings

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.openrouter_api_key,
)


def detect_intent(question: str) -> str:
    """
    Detect the user's intent.

    Returns:
        - "rag"
        - "interview_booking"
    """

    response = client.chat.completions.create(
        model="google/gemini-2.5-flash",
        temperature=0,
        max_tokens=10,
        messages=[
            {
                "role": "system",
                "content": """
You are an intent classifier.

Classify the user's request into ONE of these categories:

- rag
- interview_booking

Return ONLY one word.

Examples:

User: What is Aluminium Hydroxide?
rag

User: Explain Paracetamol dosage.
rag

User: I want to schedule an interview.
interview_booking

User: Can I book an interview for tomorrow?
interview_booking

User: I'd like to apply for this role.
interview_booking
"""
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content.strip().lower()
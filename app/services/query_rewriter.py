from openai import OpenAI

from app.config import settings

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.openrouter_api_key,
)


def rewrite_query(question: str, history: list) -> str:
    """
    Rewrite follow-up questions into standalone questions.
    """

    messages = [
        {
            "role": "system",
            "content": """
You are a query rewriting assistant.

Your task is to rewrite follow-up questions into complete,
standalone questions using the previous conversation.

Rules:
- Preserve the user's intent.
- Replace pronouns like it, they, this, that, he, she with the correct entity.
- Do NOT answer the question.
- Only return the rewritten question.
- If the question is already standalone, return it unchanged.
"""
        }
    ]

    messages.extend(history)

    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    response = client.chat.completions.create(
        model=settings.model_name,
        messages=messages,
        temperature=0,
        max_tokens=100,
    )

    return response.choices[0].message.content.strip()
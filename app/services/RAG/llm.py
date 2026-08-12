from openai import OpenAI

from app.config import settings

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.openrouter_api_key,
)


def generate(question: str, context: str, history: list):

    # System prompt
    messages = [
        {
            "role": "system",
            "content": """
You are a helpful AI assistant.

Use ONLY the retrieved context to answer the user's question.

Instructions:
- Answer in clear, natural English.
- Do not simply copy the retrieved text.
- Summarize and explain the information when appropriate.
- Use the conversation history to understand follow-up questions.
- If the question is yes/no, begin your answer with "Yes" or "No" if the context supports it.
- If the information is not available in the retrieved context, reply:
  "I don't know based on the provided information."
"""
        }
    ]

    # Add previous conversation
    messages.extend(history)

    # Current question with retrieved context
    messages.append(
        {
            "role": "user",
            "content": f"""
Retrieved Context:
{context}

Current Question:
{question}
"""
        }
    )

    response = client.chat.completions.create(
        model="google/gemini-2.5-flash",
        messages=messages,
        temperature=0,
        max_tokens=300,
    )

    return response.choices[0].message.content
from openai import OpenAI
from app.config import OPENROUTER_API_KEY

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)


def generate(question, context):

    prompt = f"""
You are a helpful assistant.

Use ONLY the retrieved context to answer the user's question.

Instructions:
- Answer in clear, natural English.
- Do not simply copy the retrieved text.
- Summarize and explain the information when appropriate.
- If the question is yes/no, begin your answer with "Yes" or "No" if the context supports it.
- If the information is not available in the context, reply:
  "I don't know based on the provided information."

Retrieved Context:
{context}

Question:
{question}"""

    response = client.chat.completions.create(
        model="google/gemini-2.5-flash",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
         temperature=0,
         max_tokens=300,
    )

    return response.choices[0].message.content
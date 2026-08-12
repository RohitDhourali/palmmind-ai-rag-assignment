from pydantic import BaseModel


from pydantic import BaseModel

class ChatRequest(BaseModel):
    session_id: str
    question: str


class ChatResponse(BaseModel):
    answer: str
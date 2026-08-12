from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.retrieval import retrieve
from app.services.retrieval import ask

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = ask(
    request.session_id,
    request.question
)

    return ChatResponse(
        answer=answer
    )
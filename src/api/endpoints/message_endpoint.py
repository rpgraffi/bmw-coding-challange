import uuid
from fastapi import APIRouter, Query
from src.api.models.chat_models import ChatResponse
from src.api.services.session_manager import SessionManager

router = APIRouter()
session_manager = SessionManager()


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(
    session_id: str = Query(default=uuid.uuid4()),
    user_message: str = Query(description="Message from the user"),
):
    assistant = session_manager.get_or_create_session(session_id)
    response = assistant.process_user_message(user_message)
    return ChatResponse(response=response)



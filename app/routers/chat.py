from fastapi import APIRouter
from app.services.chat_service import start_chat, chat_message

router = APIRouter()

@router.post("/api/chat/start")
async def start_chat_endpoint(asset_id: str):
    chat_data = start_chat(asset_id)
    return chat_data

@router.post("/api/chat/message")
async def chat_message_endpoint(chat_id: str, user_message: str):
    response = chat_message(chat_id, user_message)
    return {"response": response}

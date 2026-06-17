from fastapi import APIRouter, HTTPException
from models.message_model import Message, Save_task
from chains.chat import get_response

router = APIRouter()

@router.post('/chat')
def chat(msg: Message):
    response = get_response(msg)

    return {
        "response" : response,
        }


tasks = []

@router.post('/create_note')
def create_note(task : Save_task):
    tasks.append(task)

    return {
        "status" : HTTPException(status_code=200),
        "response" : tasks
    }
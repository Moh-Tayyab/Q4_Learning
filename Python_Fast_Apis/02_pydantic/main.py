from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from datetime import datetime, UTC
from uuid import uuid4

# Initialize the FastAPI app
app = FastAPI(
    title="DACA Chatbot API",
    description="A FastAPI-based API for a chatbot in the DACA tutorial series",
    version="0.1.0",
)


class MetaData(BaseModel):
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    session_id: str = Field(default_factory=lambda: str(uuid4()))
    
    
class Message(BaseModel):
    used_id:int
    text:str
    metadata: MetaData 
    tags: list[str] | None = None

class Response(BaseModel):
    user_id: int
    reply: str
    metadata: MetaData
    
# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the DACA Chatbot API! Access /docs for the API documentation."}    
    
# GET endpoint with query parameters
@app.get("/users/{user_id}")
async def get_user(user_id: int, role: str | None = None):
    user_info = {"user_id": user_id, "role": role if role else "guest"}
    return user_info

# POST endpoint for chatting
@app.post("/chat", response_model =Response)
async def chat(message: Message):
    if not message.text.strip():
        raise HTTPException(status_code=400, detail="Message text cannot be empty")
    reply_text = f"Hello {message.user_id}, you said: {message.text} who can I help you?"
    return Response(
        user_id = message.user_id,
        reply = reply_text,
        metadata = MetaData()  # Auto-generate timestamp and session_id
    )    
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"status": "CHAT-X online"}

@app.post("/generate")
def generate_text(req: ChatRequest):
    return {"response": f"CHAT-X принял твой текст: {req.prompt}"}

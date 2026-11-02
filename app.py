from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "CHAT-X online", "message": "Привет от твоего ИИ!"}

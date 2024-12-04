from fastapi import FastAPI
import os
from routes.livekit import livekit_routes
from app.routes.deepgram import router as deepgram_router

app = FastAPI()

app.include_router(livekit_routes)
app.include_router(deepgram_router, prefix="/deepgram", tags=["Deepgram"])


LIVEKIT_URL = os.getenv("LIVEKIT_URL")
LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
LIVEKIT_SECRET = os.getenv("LIVEKIT_SECRET")
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")

@app.get("/")
def root():
    return {"message": "Welcome to the Real-Time Interview Assistant!"}

@app.get("/livekit/token")
def get_livekit_token(identity: str, room: str):
    token = generate_livekit_token(identity, room)
    return {"token": token}



@app.get("/test-env")
def test_env():
    return {
        "LIVEKIT_URL": LIVEKIT_URL,
        "LIVEKIT_API_KEY": LIVEKIT_API_KEY,
        "LIVEKIT_SECRET": LIVEKIT_SECRET,
        "DEEPGRAM_API_KEY": DEEPGRAM_API_KEY,
        "OPENAI_API_KEY": OPENAI_API_KEY,
        "SUPABASE_URL": SUPABASE_URL,
        "SUPABASE_API_KEY": SUPABASE_API_KEY,
    }

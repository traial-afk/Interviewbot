from fastapi import FastAPI

app = FastAPI()

import os
from routes.livekit import livekit_routes

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

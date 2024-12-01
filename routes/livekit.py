from fastapi import APIRouter
from livekit import rtc
import os
import datetime

# Create the APIRouter
livekit_routes = APIRouter()

def generate_livekit_token(identity: str, room: str) -> str:
    api_key = os.getenv("LIVEKIT_API_KEY")
    api_secret = os.getenv("LIVEKIT_SECRET")
    
    if not api_key or not api_secret:
        raise ValueError("LiveKit API key or secret not set")
    
    # Create the token
    token = rtc.create_token(
        api_key=api_key,
        api_secret=api_secret,
        identity=identity,
        grants={
            "room": room,
            "can_publish": True,
            "can_subscribe": True
        }
    )
    
    return token

# Add a route for token generation
@livekit_routes.get("/token")
async def get_livekit_token(identity: str, room: str):
    token = generate_livekit_token(identity, room)
    return {"token": token}

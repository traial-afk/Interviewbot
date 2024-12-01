from livekit import rtc
import os
import datetime

def generate_livekit_token(identity: str, room: str) -> str:
    api_key = os.getenv("LIVEKIT_API_KEY")
    api_secret = os.getenv("LIVEKIT_SECRET")
    token = rtc(api_key, api_secret, identity=identity)
    token.add_grant({
        "room": room,
        "can_publish": True,
        "can_subscribe": True
    })
    token.ttl = datetime.timedelta(hours=1)  # Token valid for 1 hour
    return token.to_jwt()
import livekit
print(livekit.__file__)


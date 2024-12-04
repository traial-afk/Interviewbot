from fastapi import APIRouter, WebSocket
from deepgram import Deepgram
import os

router = APIRouter()

# Initialize Deepgram client
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
deepgram_client = Deepgram(DEEPGRAM_API_KEY)

@router.websocket("/ws/deepgram")
async def deepgram_websocket(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_bytes()
            response = await deepgram_client.transcription.live(data)
            await websocket.send_json(response)
    except Exception as e:
        await websocket.close()

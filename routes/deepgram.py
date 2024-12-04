from fastapi import APIRouter
from deepgram import Deepgram, DeepgramClient, SpeakOptions
import os
import asyncio

# Create the APIRouter
deepgram_router = APIRouter()

async def transcribe_audio(audio_url: str) -> dict:
    """
    Asynchronous function to transcribe audio using Deepgram
    
    Args:
        audio_url (str): URL of the audio file to transcribe
    
    Returns:
        dict: Transcription results
    """
    try:
        # Get Deepgram API key from environment variable
        deepgram_api_key = os.getenv("DEEPGRAM_API_KEY")
        
        if not deepgram_api_key:
            raise ValueError("Deepgram API key not set")
        
        # Initialize Deepgram client
        deepgram = Deepgram(deepgram_api_key)
        
        # Prepare source configuration
        source = {
            'url': audio_url
        }
        
        # Configure transcription options
        options = {
            'punctuate': True,
            'language': 'en-US'
        }
        
        # Perform transcription
        response = await deepgram.transcription.prerecorded.transcribe_url(source, options)
        
        return {
            "status": "success",
            "transcription": response['results']['channels'][0]['alternatives'][0]['transcript']
        }
    
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

# Route to test transcription
@deepgram_router.get("/transcribe")
async def get_transcription(audio_url: str):
    """
    API endpoint to trigger audio transcription
    
    Args:
        audio_url (str): URL of the audio file to transcribe
    
    Returns:
        dict: Transcription results
    """
    result = await transcribe_audio(audio_url)
    return result

# Optional: Simple health check route
@deepgram_router.get("/health")
async def health_check():
    """
    Health check endpoint for Deepgram router
    """
    return {
        "status": "ok",
        "service": "Deepgram Transcription"
    }

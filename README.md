app/
├── main.py            # Main FastAPI app, imports all routes and logic
├── routes/
│   ├── livekit.py     # LiveKit-related routes and utilities
│   ├── deepgram.py    # Deepgram WebSocket logic
│   ├── langchain.py   # LangChain endpoints
│   ├── supabase.py    # Supabase storage logic
├── utils/
│   ├── livekit_utils.py  # LiveKit token generation logic
│   ├── supabase_utils.py # Supabase helper functions
├── requirements.txt   # Dependencies


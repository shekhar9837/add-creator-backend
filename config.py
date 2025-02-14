import os
class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    RUNWAYML_API_KEY = os.getenv("RUNWAYML_API_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    FFmpeg_PATH = os.getenv("FFmpeg_PATH", "ffmpeg")
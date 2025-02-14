from fastapi import APIRouter, HTTPException
from services.elevenlabs import generate_voiceover
from models import VoiceoverRequest, VoiceoverResponse

router = APIRouter()

@router.post("/generate", response_model=VoiceoverResponse)
async def generate_ad_voiceover(request: VoiceoverRequest):
    try:
        audio_url = await generate_voiceover(request.text, request.voice)
        return {"audio_url": audio_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
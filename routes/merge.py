from fastapi import APIRouter, HTTPException
from services.ffmpeg import merge_video_audio
from models import MergeRequest, MergeResponse

router = APIRouter()

@router.post("/merge", response_model=MergeResponse)
async def merge_ad_video(request: MergeRequest):
    try:
        merged_video_url = await merge_video_audio(request.video_url, request.audio_url, request.music_url)
        return {"merged_video_url": merged_video_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
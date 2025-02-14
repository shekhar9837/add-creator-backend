from fastapi import APIRouter, HTTPException
from services.runwayml import generate_video
from models import VideoRequest, VideoResponse
router = APIRouter()

@router.post("/generate", response_model=VideoResponse)
async def generate_ad_video(request: VideoRequest):
    try:
        video_url = await generate_video(request.prompt, request.duration)
        return {"video_url": video_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
from typing import Union

from fastapi import FastAPI, APIRouter, HTTPException, Depends
from routes import scripts, merge, video, voiceover
from services import gemini, elevenlabs, runwayml, ffmpeg
from models import ScriptRequest, VoiceoverRequest, VideoRequest, MergeRequest, MergeResponse

app = FastAPI()
router = APIRouter()


app.include_router(scripts.router, prefix="/script", tags=["Script generator"])
app.include_router(voiceover.router, prefix="/voiceover", tags=["Voice over generator"])
app.include_router(video.router, prefix="/video", tags=["video generator"])
app.include_router(merge.router, prefix="/merge", tags=["video merge"])

@app.post("/generate-ad", response_model=MergeResponse)
async def generate_ad(prompt: str, voice: str, duration: int):
    try:
        script_request = ScriptRequest(prompt=prompt)  
        script_response = await gemini.generate_script(prompt)  

        voiceover_request = VoiceoverRequest(text=script_response["script"], voice=voice)
        voiceover_response = await elevenlabs.generate_voiceover(voiceover_request.model_dump())

        # video_request = VideoRequest(prompt=prompt, duration=duration)
        # video_response = await runwayml.generate_video(video_request.model_dump())

        # merge_request = MergeRequest(
        #     video_url=video_response["video_url"],
        #     audio_url=voiceover_response["audio_url"],
        #     music_url=""
        # )
        # merged_video_response = await ffmpeg.merge_video_audio(merge_request.model_dump())

        return {"merged_video_url": script_response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
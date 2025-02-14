from pydantic import BaseModel

class ScriptRequest(BaseModel):
    prompt: str
class ScriptResponse(BaseModel):
    script: str
class VoiceoverRequest(BaseModel):
    text: str
    voice: str 
class VoiceoverResponse(BaseModel):
    audio_url: str
class VideoRequest(BaseModel):
    prompt: str
    duration: int
class VideoResponse(BaseModel):
    video_url: str\
    
class MergeRequest(BaseModel):
    video_url: str
    audio_url: str
    music_url: str
class MergeResponse(BaseModel):
    merged_video_url: str
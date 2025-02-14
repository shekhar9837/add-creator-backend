from fastapi import APIRouter, HTTPException
from services.gemini import generate_script
from models import ScriptRequest, ScriptResponse

router = APIRouter()

@router.post("/generate", response_model=ScriptResponse)
async def generate_ad_script(request: ScriptRequest):
    try:
        script = await generate_script(request.prompt)
        return {"script": script}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
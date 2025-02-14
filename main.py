from typing import Union

from fastapi import FastAPI, APIRouter
from routes import scripts, merge, video, voiceover

app = FastAPI()
router = APIRouter()


app.include_router(scripts.router, prefix="/script", tags=["Script generator"])
app.include_router(voiceover.router, prefix="/voiceover", tags=["Voice over generator"])
app.include_router(video.router, prefix="/video", tags=["video generator"])
app.include_router(merge.router, prefix="/merge", tags=["video merge"])



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
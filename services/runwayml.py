import requests

async def generate_video(prompt: str, duration: int) -> str:
    response = requests.post("https://api.runwayml.com/v1/videos", json={"prompt": prompt, "duration": duration})

    return response.json().get("video_url", "")
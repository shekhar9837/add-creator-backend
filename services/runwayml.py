import requests

async def generate_video(prompt: str, duration: int) -> str:
    response = requests.post("https://api.runwayml.com/v1/videos", json={"prompt": prompt, "duration": duration})
    print("resposne", response)


    response.raise_for_status()
    return response.json()["video_url"]
import requests


async def generate_voiceover(text: str, voice: str) -> str:
    response = requests.post("https://api.elevenlabs.io/v1/text-to-speech", json={"text": text, "voice": voice})
    return response.json().get("audio_url", "")
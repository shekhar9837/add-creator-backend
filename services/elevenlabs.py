import boto3
import requests
from config import Config
from fastapi.responses import StreamingResponse
import io
import uuid
import os

# Initialize Amazon Polly client
polly = boto3.client(
    "polly",
    region_name='us-east-1',  # Example: 'us-east-1'
    aws_access_key_id=Config.AWS_ACCESS_KEY,
    aws_secret_access_key=Config.AWS_SECRET_KEY
)

async def generate_voiceover(text: str, voice_id: str = "Joanna") -> str:
    """
    Generates a voiceover using Amazon Polly and saves it as an MP3 file.
    """
    try:
        # Convert text to speech using Amazon Polly
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId=voice_id
        )

        # Generate unique file name
        save_file_path = f"{uuid.uuid4()}.mp3"

        # Save the audio stream as a file
        with open(save_file_path, "wb") as f:
            f.write(response["AudioStream"].read())

        print(f"{save_file_path}: A new audio file was saved successfully!")
        return save_file_path

    except requests.exceptions.RequestException as e:
        print(f"Error generating voiceover: {str(e)}")
        raise

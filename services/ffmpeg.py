import subprocess
async def merge_video_audio(video_url: str, audio_url: str, music_url: str) -> str:
    output_file = "merged_video.mp4"
    command = f"ffmpeg -i {video_url} -i {audio_url} -i {music_url} -filter_complex '[1:a]volume=0.8[a1];[2:a]volume=0.5[a2];[a1][a2]amix=inputs=2[aout]' -map 0:v -map '[aout]' -c:v copy -c:a aac {output_file}"
    subprocess.run(command, shell=True, check=True)
    return output_file
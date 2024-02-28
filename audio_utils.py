import io
import requests
import pygame.mixer

def play_audio(audio_content_bytes):
    pygame.mixer.init()
    audio_data = io.BytesIO(audio_content_bytes)
    pygame.mixer.music.load(audio_data)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def synthesize_speech(text, neets_api_key, speed=1):
    response = requests.post(url="https://api.neets.ai/v1/tts", headers={"Content-Type": "application/json", "X-API-Key": neets_api_key},
                             json={"text": text, "voice_id": "vits-rus-1", "params": {"model": "vits"}})
    return response.content if response.status_code == 200 else None

import openai
import base64
from io import BytesIO

async def speech_to_text(audio_base64: str) -> str:
    audio_bytes = base64.b64decode(audio_base64)
    with open("temp.wav", "wb") as f:
        f.write(audio_bytes)

    transcript = openai.Audio.transcriptions.create(
        model="whisper-1",
        file=open("temp.wav", "rb")
    )
    return transcript.text

async def text_to_speech(text: str) -> str:
    response = openai.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text
    )
    audio_bytes = response.read()
    return base64.b64encode(audio_bytes).decode("utf-8")  
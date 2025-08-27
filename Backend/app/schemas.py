from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]

class VoiceRequest(BaseModel):
    audio_base64: str  # send audio from frontend as base64 string

class VoiceResponse(BaseModel):
    text: str
from fastapi import FastAPI
# from .schemas import QueryRequest, QueryResponse, VoiceRequest, VoiceResponse
# from .rag_service import rag_pipeline
# from .voice_service import speech_to_text, text_to_speech
from .routes.text_response import router as text_response_router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)
# @app.post("/query", response_model=QueryResponse)
# async def query_rag(req: QueryRequest):
#     answer, sources = rag_pipeline(req.query)
#     return QueryResponse(answer=answer, sources=sources)

# @app.post("/voice-to-text", response_model=VoiceResponse)
# async def voice_to_text(req: VoiceRequest):
#     text = await speech_to_text(req.audio_base64)
#     return VoiceResponse(text=text)

# @app.post("/text-to-voice")
# async def text_to_voice(req: QueryRequest):
#     audio_base64 = await text_to_speech(req.query)
#     return {"audio_base64": audio_base64}

app.include_router(text_response_router, prefix="/text-response", tags=["Text Response"])
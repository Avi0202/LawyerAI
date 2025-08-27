from fastapi import APIRouter
from ..schemas import QueryRequest, QueryResponse
from ..rag_service import rag_pipeline
router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def query_rag(req: QueryRequest):
    # Placeholder implementation
    answer,sources = rag_pipeline(req.query)
    return QueryResponse(answer=answer, sources=sources)
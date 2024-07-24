from fastapi import APIRouter
from src.app.schemas.query import QueryRequest, QueryResponse
from src.rag.components.query_engine import query_engine

router = APIRouter(
    prefix="/query",
)

@router.post("/", response_model=QueryResponse)
def query(query_request: QueryRequest) -> QueryResponse:
    response = query_engine.query(query_request.txt) 
    return QueryResponse(txt=response.response)

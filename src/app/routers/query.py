from fastapi import APIRouter
from src.app.schemas.query import QueryRequest, QueryResponse
from src.rag.components.query_engine import query_engine

router = APIRouter(
    prefix="/query",
)

# @router.post("/", response_model=QueryResponse)
# async def query(query_request: QueryRequest):
#     response = await query_engine.aquery(query_request.txt) 
#     return QueryResponse(txt=response.response)


@router.post("/", response_model=str)
def query(query_request: str):
    response = query_engine.query(query_request) 
    return response.response
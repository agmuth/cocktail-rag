from pydantic import BaseModel


class QueryRequest(BaseModel):
    txt: str


class QueryResponse(BaseModel):
    txt: str

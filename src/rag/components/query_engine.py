from llama_index.core import VectorStoreIndex

from src.rag.components.embed_model import embed_model
from src.rag.components.llm import llm
from src.rag.components.vector_store import vector_store

query_engine = VectorStoreIndex.from_vector_store(
    vector_store=vector_store, embed_model=embed_model
).as_query_engine(llm=llm)

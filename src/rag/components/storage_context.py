from llama_index.core import StorageContext

from src.rag.components.document_store import document_store
from src.rag.components.vector_store import vector_store

storage_context = StorageContext.from_defaults(
    docstore=document_store, vector_store=vector_store
)

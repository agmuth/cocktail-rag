from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter

from src.rag.components.document_store import document_store
from src.rag.components.embed_model import embed_model
from src.rag.components.vector_store import vector_store

pipeline = IngestionPipeline(
    transformations=[SentenceSplitter(), embed_model],
    docstore=document_store,
    vector_store=vector_store,
)

import qdrant_client
from llama_index.vector_stores.qdrant import QdrantVectorStore

from src.rag.components.embed_model import embed_model
from src.settings import BASE_SETTINGS

client = qdrant_client.QdrantClient(
    host=BASE_SETTINGS.QDRANT_HOST, port=BASE_SETTINGS.QDRANT_PORT
)
vector_store = QdrantVectorStore(
    client=client, collection_name="example", embed_model=embed_model
)

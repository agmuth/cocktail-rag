import qdrant_client
from llama_index.vector_stores.qdrant import QdrantVectorStore

from src.rag.components.embed_model import embed_model
from src.settings import BASE_SETTINGS

client = qdrant_client.QdrantClient(url=BASE_SETTINGS.QDRANT_URL)
vector_store = QdrantVectorStore(
    collection_name=BASE_SETTINGS.QDRANT_COLLECTION_NAME,
    client=client,
    embed_model=embed_model,
)

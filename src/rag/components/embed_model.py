from llama_index.embeddings.ollama import OllamaEmbedding

from src.settings import BASE_SETTINGS

embed_model = OllamaEmbedding(
    model_name=BASE_SETTINGS.OLLAMA_LLM,
    base_url=BASE_SETTINGS.OLLAMA_BASE_URL,
)

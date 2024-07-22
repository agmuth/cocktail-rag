from llama_index.embeddings.ollama import OllamaEmbedding

from src.settings import BASE_SETTINGS

embed_model = OllamaEmbedding(BASE_SETTINGS.OLLAMA_LLM)

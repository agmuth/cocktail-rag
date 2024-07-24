from llama_index.llms.ollama import Ollama

from src.settings import BASE_SETTINGS

llm = Ollama(
    model=BASE_SETTINGS.OLLAMA_LLM,
    host=BASE_SETTINGS.OLLAMA_HOST,
    port=BASE_SETTINGS.OLLAMA_PORT,
    base_url=BASE_SETTINGS.OLLAMA_BASE_URL,
    request_timeout=60 * 2,
)
# llm = None

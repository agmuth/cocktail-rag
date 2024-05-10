

from llama_index.llms.ollama import Ollama

llama = Ollama(
    model="phi",
    request_timeout=300.0,
)

resp = llama.complete("hi")

print(resp)
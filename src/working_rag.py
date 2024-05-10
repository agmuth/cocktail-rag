from settings import BASE_SETTINGS

from llama_index.core import SimpleDirectoryReader
import os.path
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
    Settings,
)
from llama_index.embeddings.ollama import OllamaEmbedding

from llama_index.llms.ollama import Ollama

Settings.llm = Ollama(model="phi", request_timeout=60*2)
Settings.embed_model = OllamaEmbedding("phi")
 
# check if storage already exists
if not os.path.exists(BASE_SETTINGS.PERSIST_DIR):
    # load the documents and create the index
    loader = SimpleDirectoryReader(
        input_dir=BASE_SETTINGS.DATA_DIR, 
        recursive=True,
    )
    documents = loader.load_data(show_progress=True)

    from random import sample
    n = 1000
    documents = sample(documents, n)
    

    index = VectorStoreIndex.from_documents(
        documents,
        # embed_model=embedding_model,
        show_progress=True,
    )
    # store it for later
    index.storage_context.persist(persist_dir=BASE_SETTINGS.PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(
        persist_dir=BASE_SETTINGS.PERSIST_DIR,
        
    )
    index = load_index_from_storage(storage_context)


query_engine = index.as_query_engine()

query = "Please recommend me a Fancy cocktail. Include a list of ingredients and instructions for how to make it."
response = query_engine.query(query)
print(response)
pass

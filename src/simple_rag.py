from llama_index.core import (
    ServiceContext,
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
    set_global_service_context,
)
from llama_index.llms.ollama import Ollama
from settings import BASE_SETTINGS

llm = Ollama(model="llama2")

# Reads pdfs at "./" path
documents = (
    SimpleDirectoryReader(
        input_dir = BASE_SETTINGS.DATA_DIR,
        required_exts = [".txt"])
        .load_data()
)

# ServiceContext is a bundle of commonly used 
# resources used during the indexing and 
# querying stage 
service_context = (
    ServiceContext
    .from_defaults(
        llm=llm, 
        embed_model="local:BAAI/bge-small-en-v1.5", 
        chunk_size=300
    )
)
set_global_service_context(service_context)

# Node represents a “chunk” of a source Document
nodes = (
    service_context
    .node_parser
    .get_nodes_from_documents(documents)
)

# offers core abstractions around storage of Nodes, 
# indices, and vectors
storage_context = StorageContext.from_defaults()
storage_context.docstore.add_documents(nodes)

# Create the vectorstore index
index = (
    VectorStoreIndex
    .from_documents(
        documents, 
        storage_context=storage_context, 
        llm=llm
        )
)
query_engine = index.as_query_engine()

# Query the index
query="""What kind of vermouth do I need to use in a martini cocktail?"""
response = query_engine.query(query)
print(response)
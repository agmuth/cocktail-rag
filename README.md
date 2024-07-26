# cocktail-rag

## Steps:
1. Install project with command: `make install`.
2. Scrape cockatils with command: `make scrape`.
3. Stand up services with command: `docker compose up`.
4. Populate vector DB with command: `docker exec -it api poetry run python src/rag/scripts/init_vector_store.py <num_docs_to_ingest>`.
5. Open UI at https://localhost:8080.



Example `.env` file:

```{}
DATA_DIR=data
PERSIST_DIR=storage

OLLAMA_HOST=ollama
OLLAMA_PORT=11434
OLLAMA_LLM=phi3

MONGO_HOST=mongo
MONGO_PORT=27017
MONGO_DB_NAME=cocktails_db

MONGOEXPRESS_HOST=mongo-express
MONGOEXPRESS_PORT=8081

QDRANT_HOST=qdrant
QDRANT_PORT=6333
QDRANT_COLLECTION_NAME=cocktails_collection

API_HOST=api
API_PORT=8000

UI_HOST=ui
UI_PORT=8080
```
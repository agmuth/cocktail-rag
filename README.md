# cocktail-rag

run the command below once all services are up to init the vector db
`docker exec -it api poetry run python src/rag/scripts/init_vector_store.py <num_docs_to_ingest>`
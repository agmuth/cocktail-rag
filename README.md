# cocktail-rag


docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama && \
docker exec -it ollama ollama run phi \
&& /bye

docker exec -it app poetry run python src/rag/scripts/init_vector_store.py 10
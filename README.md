# cocktail-rag


docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama && \
docker exec -it ollama ollama run phi \
&& /bye
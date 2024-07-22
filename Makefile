format:
	poetry run black src/
	poetry run isort src/

	
lint: 
	poetry run ruff check src/. --fix


ollama:
	docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama \
	&& docker exec -d ollama ollama run phi
format:
	poetry run black src/
	poetry run isort src/

	
lint: 
	poetry run ruff check src/. --fix

install:
	poetry install

scrape:
	poetry run python src/scripts/cocktail_friend_scraper.py
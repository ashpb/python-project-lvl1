build:
	poetry build

install:
	poetry install

publish:
	poetry publish -r testpypi

lint:
	poetry run flake8 brain_games

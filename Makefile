setup:
	pip install -r requirements.txt

format:
	black .
	isort .

lint:
	env PYTHONPATH=. pytest --flake8 --pylint --mypy

utest:
	env PYTHONPATH=. pytest ./tests/ -s --verbose

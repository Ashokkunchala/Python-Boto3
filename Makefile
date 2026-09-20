install:
	python -m pip install -r requirements-dev.txt
	python -m pip install -e .

test:
	pytest

lint:
	ruff check .

typecheck:
	mypy src

check: lint test

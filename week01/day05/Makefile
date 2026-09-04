.PHONY: format lint run all

all: format lint run

format:
	black .
	isort .

lint:
	pylint energy_insights tests

run:
	python3 -m pytest tests/test.py

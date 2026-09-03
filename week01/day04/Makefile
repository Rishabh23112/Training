.PHONY: format lint run all

all: format lint run

format:
	black .
	isort .

lint:
	pylint energy_insights

run:
	python -m energy_insights --file data/energy/hourly_prices.csv

all: deps unit lint
.PHONY: all

deps:
	[ -d venv ] || python3 -m venv ./venv
	. ./venv/bin/activate
	pip install -r requirements.txt
.PHONY: deps

unit: deps
	python3 manage.py test
.PHONY: unit

lint: deps
	echo "TODO: add linters"
.PHONY: lint

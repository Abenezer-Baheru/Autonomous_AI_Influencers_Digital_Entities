SHELL := /bin/bash
VENV := .venv
PY := $(VENV)/Scripts/python.exe
PIP := $(VENV)/Scripts/pip.exe

.PHONY: setup test lint docker-build docker-run spec-check

setup:
	@test -d $(VENV) || python -m venv $(VENV)
	@echo "Installing package and test deps into $(VENV)"
	@$(PIP) install --upgrade pip setuptools wheel || python -m pip install --upgrade pip setuptools wheel
	@$(PIP) install -e . pytest

test:
	@echo "Running pytest..."
	@$(PY) -m pytest -q

lint:
	@echo "Linting JSON files..."
	@python -m json.tool .vscode/mcp.json || true

docker-build:
	@echo "Building Docker image 'project-chimera:latest'"
	@docker build -t project-chimera:latest .

docker-run:
	@docker run --rm -it project-chimera:latest bash

spec-check:
	@echo "Spec-check placeholder: ensure specs/ files exist"
	@test -d specs || (echo "specs/ missing" && false)

# ==========================================================
# Sportsbook Engine
# Development Commands
# ==========================================================

.DEFAULT_GOAL := help

.PHONY: help install dev test lint format typecheck check clean


help:
	@echo ""
	@echo "Sportsbook Engine"
	@echo ""
	@echo "Available commands:"
	@echo "  make dev        Install development dependencies"
	@echo "  make install    Install runtime dependencies"
	@echo "  make test       Run test suite"
	@echo "  make lint       Run Ruff"
	@echo "  make format     Format code with Black"
	@echo "  make typecheck  Run MyPy"
	@echo "  make check      Run all quality checks"
	@echo "  make clean      Remove generated cache files"
	@echo ""


install:
	pip install -e .


dev:
	pip install -e ".[dev]"

run:
	python -m scripts.main

test:
	pytest


lint:
	ruff check .


format:
	black .


typecheck:
	mypy sportsbook


check:
	ruff check .
	black --check .
	mypy sportsbook
	pytest


clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
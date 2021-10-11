.DEFAULT_GOAL := help
SHELL := /bin/bash
EXECUTABLES = poetry
K := $(foreach exec,$(EXECUTABLES),\
        $(if $(shell which $(exec)),some string,$(error "You must install $(exec) to use this Makefile")))

.PHONY: help
help: ## Install make to use this file, then write "make [command]".
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: all 
all: clean install_dependencies update_dependencies lint test install

.PHONY: install_dependencies
install_dependencies: ## Install dependencies
	poetry install --no-root

.PHONY: update_dependencies
update_dependencies: ## Update dependencies
	poetry update
	poetry install --no-root

.PHONY: shell
shell: ## Enter poetry virtualenv
	poetry shell

.PHONY: install
install: ## Install package into virtualenv
	poetry install

.PHONY: lint
lint: install_dependencies ## Run black and isort (delete/add more as appropriate)
	poetry run isort --profile=black --lines-after-imports=2 ./tests/ ./src/
	poetry run black ./tests/ ./src/

.PHONY: style_check
style_check: install_dependencies ## Return diff of code for styling check
	@echo "flake8:"; if (! poetry run flake8 ./tests/ ./src/); then ERROR=true; fi; \
	echo ""; \
	echo "isort:"; if (! poetry run isort --diff --check-only --profile=black --lines-after-imports=2 ./tests/ ./src/); then ERROR=true; fi; \
	echo ""; \
	echo "black:"; if (! poetry run black --diff --check ./tests/ ./src/); then ERROR=true; fi; \
	echo ""; \
	if [ "$$ERROR" = "true" ]; then echo "Styling error detected, failing" && exit 1; fi

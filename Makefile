.PHONY: clean install-venv create-venv requirements run

.DEFAULT_GOAL := help

help: ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@awk -F ':.*?## ' '/^[a-zA-Z]/ && NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean: ## remove generated byte code, coverage reports, and build artifacts
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	rm -rf translations

install-venv: ## install virtualenv
	pip install virtualenv 

create-venv: ## create a virtual environment on the project root
	virtualenv -p python3 .venv

requirements: ## install project requirements in a virtualenv
	. .venv/bin/activate; pip install -r requirements.txt   

get: ## run application
	. .venv/bin/activate; python main.py ${lang}

get-all: ## download all translations
	. .venv/bin/activate; python main.py all
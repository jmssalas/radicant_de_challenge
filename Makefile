.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

CURDIR=$(shell pwd)
WORKDIR=/usr/src/myapp
DOCKER_RUN=docker run -it -v $(CURDIR):$(WORKDIR) -w $(WORKDIR) -p 8000:8000 python bash -c

enter: ## Enter into the docker
	$(DOCKER_RUN) "pip install -r requirements.txt; bash"

run: ## Run Django server into the docker
	$(DOCKER_RUN) "pip install -r requirements.txt; python radicant/manage.py runserver 0.0.0.0:8000"

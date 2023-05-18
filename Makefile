.PHONY: help
.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

build: # Build the project image
	@echo "--> Building Compose"
	docker compose build

build-no-cache: # Build the project image ignoring the cache
	@echo "--> Building Compose"
	docker compose build --no-cache

run: # Runs the project
	@echo "--> Running the project"
	docker compose up

kill:
	@echo "--> Killing the container"
	docker compose down

test: # Run tests
	@echo "--> Testing on Docker."
	docker compose run app pytest $(path) -s

migrate: # Run migrations
	@echo "--> Building Compose"
	docker compose run python manage.py migrate
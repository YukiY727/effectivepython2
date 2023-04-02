.PHONY: build up down

build:
	docker build -t effective_python .

up:
	docker run -it --rm -v "$(pwd)":/app effective_python bash

# Down target
down:
	docker stop effective_python_container

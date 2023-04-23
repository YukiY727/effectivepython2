IMAGE_NAME = effective_python
.PHONY: build up down

build:
	docker build -t $(IMAGE_NAME) .

up:
	docker run -it --rm -v "$(pwd)":/app ${IMAGE_NAME} bash

# Down target
down:
	docker stop effective_python_container

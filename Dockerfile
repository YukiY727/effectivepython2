FROM python:3.11-slim-buster AS base

RUN apt-get update && \
    pip install poetry && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /effective_python_docker
# copy toml and lock files
COPY . /effective_python_docker/


# # Stage 1: Base image
# FROM python:3.11-slim-buster AS base

# RUN apt-get update && \
#     apt-get install -y git && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/* && \
#     pip install poetry

# WORKDIR /effective_python_docker

# # Stage 2: Builder image
# FROM base AS builder

# COPY pyproject.toml poetry.lock /effective_python_docker/

# RUN poetry config virtualenvs.create false && \
#     poetry install --no-interaction --no-ansi --no-root

# # Stage 3: Final image
# FROM base AS final

# COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
# COPY . /effective_python_docker/


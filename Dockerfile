FROM python:3.11-slim-buster AS base

RUN apt-get update && \
    pip install poetry

WORKDIR /effective_python_docker
# copy toml and lock files
COPY . /effective_python_docker/

# install dependencies
RUN poetry config virtualenvs.create true && \
    poetry install --no-interaction --no-ansi

# RUN poetry config virtualenvs.create false && \
#     poetry install --no-interaction --no-ansi


# COPY . /effective_python_docker/
# FROM python:3.11-slim-buster AS runner

# RUN apt-get update && \

# copy poetry environment from base image
# COPY --from=base /root/.local /root/.local

# copy project files



# FROM python:3.9-slim-buster AS builder
# ENV PYTHONUNBUFFERED 1

# RUN apt-get update && \
#     apt-get install -y gcc libpq-dev

# RUN python -m venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"

# WORKDIR /code
# COPY requirements/ /code/

# RUN pip install --upgrade pip
# RUN pip install -r production.txt


# FROM python:3.9-slim-buster AS runner
# RUN apt-get update && \
#     apt-get install -y libpq-dev

# COPY --from=builder /opt/venv /opt/venv

# WORKDIR /code
# COPY . /code/

# RUN useradd -ms /bin/bash nonroot
# USER nonroot

# ENV PATH="/opt/venv/bin:$PATH"
# Pull base image
FROM python:3.11 as builder

RUN pip install poetry==2.1.3

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app
    
COPY ./pyproject.toml ./poetry.lock README.md ./
    
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

FROM python:3.11-slim as runtime

COPY . ./app

EXPOSE 8000
# ENTRYPOINT ["poetry", "run", "python", "-m", "app.main"]
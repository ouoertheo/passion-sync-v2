# https://medium.com/@albertazzir/blazing-fast-python-docker-builds-with-poetry-a78a66f5aed0
FROM python:3.11-alpine

RUN apk add gcc musl-dev linux-headers python3-dev
RUN pip install poetry==2.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1\
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-cache

COPY passion_sync ./passion_sync

RUN touch README.md
RUN poetry install --no-cache


# Run the application.
CMD poetry run passion
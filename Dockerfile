FROM python:3.9-slim

ENV PIP_DIABLE_PIP_VERSION_CHECK=on
ENV PIP_TIMEOUT=60

RUN pip install  "poetry==1.7.1"

WORKDIR /app

COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction


COPY src/ /app
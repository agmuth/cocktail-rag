# FROM python:3.9-slim

# RUN pip install  "poetry==1.7.1"

# RUN pip install poetry==1.7.1

# ENV POETRY_NO_INTERACTION=1 \
#     POETRY_VIRTUALENVS_IN_PROJECT=1 \
#     POETRY_VIRTUALENVS_CREATE=1 \
#     POETRY_CACHE_DIR=/tmp/poetry_cache


# WORKDIR /app
# COPY data/ ./data/

# RUN touch README.md
# COPY pyproject.toml poetry.lock ./
# RUN poetry install --no-root --without dev 

# COPY src/ ./src/
# RUN poetry install --only-root
# RUN rm -rf $POETRY_CACHE_DIR

# # grdio specific
# EXPOSE 7860
# ENTRYPOINT ["poetry", "run", "python", "src/ui/ui.py"]
# # ENTRYPOINT ["tail", "-f", "/dev/null"]


FROM python:3.9-slim

RUN pip install  "poetry==1.7.1"

RUN pip install poetry==1.7.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache


WORKDIR /app
COPY data/ ./data/

RUN touch README.md
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --without dev 

COPY src/ ./src/
RUN poetry install --only-root
RUN rm -rf $POETRY_CACHE_DIR

# grdio specific
EXPOSE 8000
CMD ["poetry", "run", "fastapi", "run", "src/app/main.py", "--port", "8000"]
# CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
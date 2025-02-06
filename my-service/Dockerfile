FROM python:3.9-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY src/ ./src/

CMD ["poetry", "run", "uvicorn", "my_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-interaction --no-ansi --no-root

COPY . .

CMD ["poetry", "run", "uvicorn", "my_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
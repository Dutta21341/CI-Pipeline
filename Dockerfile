FROM python:3.12
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN pip install poetry && poetry install --no-root
COPY . /app/
CMD ["poetry", "run", "python", "main.py"]

FROM python:3.9

RUN apt-get update && apt-get install -y netcat

WORKDIR /code

COPY ./pyproject.toml ./

RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000
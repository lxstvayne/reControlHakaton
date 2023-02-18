FROM python:3.10-slim-buster


WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2-binary

RUN pip install --upgrade pip

COPY ./pyproject.toml .

RUN pip install poetry

RUN poetry install

COPY . .

CMD [ "poetry", "run", "python", "./manage.py", "runserver", "0.0.0.0:80"]
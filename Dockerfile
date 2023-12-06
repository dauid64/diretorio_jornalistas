FROM python:3.11.3-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY app /app

WORKDIR /app

RUN pip install -r requirements_docker.txt
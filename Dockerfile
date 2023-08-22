FROM python:3.11.3-alpine3.18
LABEL mantainer="carlosdauid64br@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY app /app
COPY scripts /scripts

WORKDIR /app

EXPOSE 8000

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /app/requirements.txt && \
    adduser --disabled-password --no-create-home duser && \
    mkdir -p /data/web/static && \
    mkdir -p /data/web/media

ENV PATH="/scripts:/venv/bin:$PATH"

CMD ["commands.sh"]
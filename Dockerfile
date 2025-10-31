FROM python:3.14-slim-bookworm

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y libpq-dev gcc curl && rm -rf /var/lib/apt/lists/*
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | sh - && apt install -y nodejs && npm install -g npm@latest
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt && pip install gunicorn

COPY . .

RUN cd theme/static_src && npm install && npm run build
RUN python manage.py collectstatic --noinput

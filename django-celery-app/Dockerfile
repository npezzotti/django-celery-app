FROM python:3.10.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add postgresql-dev \
        gcc python3-dev \
        musl-dev \
        build-base \
        linux-headers \
        pcre-dev

WORKDIR /app

RUN python -m pip install --upgrade pip 
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh
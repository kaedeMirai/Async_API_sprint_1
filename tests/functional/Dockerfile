FROM python:3.11

WORKDIR /tests/functional

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /tests/functional/
COPY __init__.py /tests/

RUN apt-get update \
    && pip install --no-cache-dir -r /tests/functional/requirements.txt

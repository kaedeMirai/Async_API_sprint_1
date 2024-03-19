FROM python:3.11

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app

RUN apt-get update \
    && apt-get install -y netcat-traditional \
    && pip install --no-cache-dir -r requirements.txt

WORKDIR /app/src

CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker \
    --bind=$FASTAPI_HOST:$FASTAPI_PORT --access-logfile - --error-logfile -

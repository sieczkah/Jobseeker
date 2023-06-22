FROM python:3.11.4-alpine3.17

LABEL maintainer="https://siehub.site/"


ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt
RUN apk add --upgrade --no-cache build-base linux-headers && \
    pip install --upgrade pip && \
    pip install -r requirements.txt 

COPY . /app
WORKDIR /app

RUN adduser --disabled-password --no-create-home django && \
    chmod -R +x ./scripts


ENV PATH="/scripts:$PATH"
USER django
CMD ["run.sh"]


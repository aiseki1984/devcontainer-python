FROM python:3.10.5
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y zlib1g-dev libzip-dev libpq-dev mariadb-client tzdata zip unzip git

WORKDIR /workspace

ADD requirements.txt /workspace
RUN pip install -r requirements.txt
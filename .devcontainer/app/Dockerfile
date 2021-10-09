FROM python:3
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y zlib1g-dev libzip-dev libpq-dev mariadb-client tzdata zip unzip git

WORKDIR /var/www/html

ADD requirements.txt /var/www/html
RUN pip install -r requirements.txt
FROM python:3.13-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip3 install --upgrade pip
RUN pip3 install pipenv
RUN pipenv install --system --deploy

WORKDIR /usr/src/app

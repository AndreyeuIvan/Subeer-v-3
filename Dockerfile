FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /django_subeer

WORKDIR /django_subeer

COPY . .

RUN python3 -m pip install --upgrade pip

COPY ./req.txt /req.txt

RUN pip3 install -r /req.txt



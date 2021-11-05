FROM python:3.8.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /account

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
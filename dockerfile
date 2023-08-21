# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 1000

CMD [ "python3", "./src/app/main.py"]
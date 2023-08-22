# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 10000

CMD [ "python3", "./src/app/main.py"]

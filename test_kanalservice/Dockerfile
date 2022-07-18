FROM python:3.9.5-slim

WORKDIR /app

RUN apt-get update
RUN apt-get -y install python-pip
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install psycopg2-binary

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .
CMD cd test_kanalservice && gunicorn test_kanalservice.wsgi:application --bind 0.0.0.0:8000
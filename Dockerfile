# Pull the base image
FROM python:3.10.12-slim-buster

# SET ENVIRONMENT VARIABLES
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

WORKDIR /code
RUN pip install requests

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# COPY PROJECT
COPY . .
